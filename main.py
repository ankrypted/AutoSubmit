import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


print("Welcome To Codeforces LogIn")
username = raw_input("Enter your Username: ")
password = raw_input("Enter your Password: ")
# helloCode = raw_input("Enter CODE: ")
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver =  webdriver.Chrome(chrome_options=options)

# driver.get("https://codeforces.com")
driver.get("https://codeforces.com/contest/1183/problem/D")

	# temp = driver.find_elements(by='button')
temp = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[1]')
temp.click()
driver.save_screenshot("URGENT.png")
inputUsername = driver.find_element_by_xpath('//*[@id="handleOrEmail"]')
inputUsername.send_keys(username)
inputPassword = driver.find_element_by_xpath('//*[@id="password"]')
inputPassword.send_keys(password)
logIn = driver.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input')
logIn.click()
time.sleep(5)
submit = driver.find_element_by_xpath('//*[@id="pageContent"]/div[1]/ul/li[3]/a')
submit.click()
# body = driver.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL + 't')
time.sleep(3)
code = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[5]/td[2]/input')
code.send_keys("/home/ankesh/ankrypt/lib/pyProjects/JustClick/sol.cpp")
# code.click()
time.sleep(10)
submitCode = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[6]/td/div/div/input')
submitCode.click()
time.sleep(30)
driver.save_screenshot("NEWURGENT.png")
driver.close()
	# driver.find_element_by_tag_name('body').send_keys(keys.COMMAND + 't')
	# body = driver.find_element_by_tag_name("body")
	# body.send_keys(Keys.CONTROL + 't')

print "Successfully Logged in as", username

# contestId = raw_input("Enter the contest id")

# print 
