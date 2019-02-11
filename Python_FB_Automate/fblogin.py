from selenium import webdriver
from getpass import getpass

user=input("Enter the User id/Email")
pas=getpass("Enter your password To login")
driver=webdriver.Chrome(executable_path=r"C:\Users\surendar\Downloads\chromedriver_win32/chromedriver.exe")
driver.get('https://www.facebook.com/')
username_box=driver.find_element_by_id('email')
username_box.send_keys(user)
pass_box=driver.find_element_by_id('pass')
pass_box.send_keys(pas)
login_btn=driver.find_element_by_id('u_0_3')
login_btn.submit()