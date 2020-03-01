from selenium import webdriver
import time
import pyautogui as py
import json
from win10toast import ToastNotifier

with open('user_config.json') as user_config:
    user = json.load(user_config)

# Time interval of 2 hours
time_interval = 2 * 60 * 60

while True:

    time.sleep(time_interval)

    toaster = ToastNotifier()
    toaster.show_toast(
        'Auto-Proxy',
        '''Auto proxy will run the scheduled proxy registration process in 30 seconds kindly do not click away from the opened browser window while the proxy registration is in progress or your username and password may get leaked.'''
    )

    # Wait for 30 seconds as mentioned in the notification
    time.sleep(30)

    if user["preffered_browser"] == "Firefox":
        driver = webdriver.Firefox()
    if user["preffered_browser"] == "Chrome":
        driver = webdriver.Chrome()
    if user["preffered_browser"] == "Opera":
        driver = webdriver.Opera()

    # driver.maximize_window()

    username = user["username"]
    password = user["password"]
    proxy = user["proxy_address"]
    driver.get("http://" + proxy)

    time.sleep(0.5)

    # Type in details
    py.typewrite(username + '\t' + password + '\n')

    time.sleep(0.5)

    # obj = driver.switch_to.alert
    # obj.send_keys(username)
    # py.typewrite('\t')
    # obj.send_keys(password)
    # py.typewrite('\n')

    driver.close()
