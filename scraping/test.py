import smtlib

# print(dir(xsmtplib))
# print(dir(smtlib.SMTP))
server = smtlib.SMTP(host="smtp.example.com", proxy_host="proxy.example.com")