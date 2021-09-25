from selenium.webdriver import Firefox
from time import sleep


browser = Firefox()
browser.get('https://web.whatsapp.com/')
sleep(5)

while len(browser.find_element_by_id('side')) < 1:
    sleep(1)
