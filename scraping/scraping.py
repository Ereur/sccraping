from time import sleep
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from wrapers import FindElements, FindElement;
from selenium.webdriver.common.keys import Keys
from instascrape import *
import random
import time
# from cookies.py import cookies
chrome_options = Options()
chrome_options.add_argument("--headless")
import json

start_time = time.time()
with open ('cookies.json', 'r') as myfile:
 data=myfile.read()

fruit_detail = json.loads(data)
# print(data);
driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
# driver.set_window_size(1853, 1240);
# driver.maximize_window();
url = "https://www.instagram.com/explore/tags/germany/"
driver.get(url)

# sleep(10);
# test = driver.get_screenshot_as_file('foo1.png');
# print(driver.page_source);

# Button = driver.find_element(By.CLASS_NAME,"_a9-- _a9_0");
# sleep(3);
# print(Button);
# print(dir(By));
# exit(1);
for cookie in fruit_detail:
    driver.add_cookie(cookie)
print(dir(driver));

driver.refresh();

# elements = FindElements(driver,"_aagw")
elements = FindElements(driver, (By.CLASS_NAME, "_aagw"), 10)
if elements == False:
    print("chi haja machi hya hadik")
    exit(1)

ele =   FindElement(driver, (By.TAG_NAME, 'body'));
def remove_dupiclates(list_):
    new_list = []
    for a in list_:
        if a not in new_list:
            new_list.append(a)
    return new_list

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

links = []
names = []
CleanName = []
parent = driver.window_handles[0];
file = open("links.csv","w")
times = open("counter", "w")
timesofscroll = 0
while True :
    posts = FindElements(driver, (By.CLASS_NAME, "_aabd._aa8k._aanf"), 10)
    for post in posts:
        tag = post.find_element(By.TAG_NAME, "a")
        links.append(tag.get_attribute("href"));
        # print(tag.get_attribute("href"))
        # print(post.cli)
    links = remove_dupiclates(links);
    # if len(links) > 500:
    #     break;
    
    n = random.random()
    print(len(links));
    sleep(n)
    if len(links) > 1000:
        for link in links:
            file.write(link + '\n')
        links = []
        n = random.randint(1, 6)
        # sleep(n)
    if time.time() - start_time > 120:
        sleep(random.randint(1, 20))
        print('scroling')
        driver.execute_script("window.scrollBy(0, -500);")
        start_time = time.time()
    ele.send_keys(Keys.END)
    timesofscroll += 1
    times.write(str(timesofscroll) + "\n")
file = open("links.csv","r")
links = file.readlines()
for link in links:
    string = 'window.open(\'' + link + '\');';
    driver.execute_script(string);
    driver.switch_to.window(driver.window_handles[1])
    while True:
        button = FindElement(driver, (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button"));
        if button == False:
            break;
        button.click();
        sleep(1);
    comments = FindElements(driver, (By.CLASS_NAME, "_a9zc"), 10);
    if comments == False:
        print("chi haja machi hya hadik f comments")
        exit(1)
    for comment in comments:
        names.append(comment.text);
    names = remove_dupiclates(names);
    # if len(names) > 10:
    #     driver.close();
    #     driver._switch_to.window(parent);
    #     break;
    driver.close();
    driver._switch_to.window(parent);
file = open("names.txt","w")
i = 0
for name in names:
    string = 'window.open(\'https://www.instagram.com/'+ name + '\');'
    print(string);
    driver.execute_script(string);
    driver.switch_to.window(driver.window_handles[1])
    ProfileName = FindElement(driver, (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/span"))
    if ProfileName == False:
        driver.close();
        driver._switch_to.window(parent);
        continue
    tmp = ProfileName.text + '\n'
    file.write(tmp)
    driver.close();
    driver._switch_to.window(parent);
    i += 1
sleep(60);
    # driver.back();

# print(len(comments));
# print(len(elements));
# print(dir(driver));
test = driver.get_screenshot_as_file('foo.png');

# url = "https://www.instagram.com/explore/tags/germany/"
# driver.get(url)
# sleep(4);
# test = driver.get_screenshot_as_file('foo.png');
# test.contains();
# test.save_screenshot('screen.png');
# print(dir(driver));
driver.quit()
exit(1);
h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
print(h1)

# browser.quit()