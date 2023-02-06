from selenium.common.exceptions import TimeoutException, NoSuchElementException;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located, element_to_be_clickable;
def FindElements(driver, selector, timout):
	try:
		elements = WebDriverWait(driver,timout).until(visibility_of_all_elements_located(selector));
	except TimeoutException:
		return False;
	return elements;

def FindElement(driver, selector):
	try:
		element = WebDriverWait(driver,3).until(element_to_be_clickable(selector));
	except TimeoutException:
		print("waaa3");
		return(False);
	return element;