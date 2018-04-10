from selenium import webdriver
from time import sleep

#config
profile=webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150) #tor proxy port

#Begin browse
browser=webdriver.Firefox(profile)
browser.get("https://miip.es/")
browser.save_screenshot("ip.png")
sleep(5)

browser.close()

