from selenium import webdriver
from selenium.webdriver.ie.service import Service


browser = input('what browser do you want to use?')

match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
    case _:
        print('Unknown browser - Not available. \n Executing with default EDGE browser.')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get('https://www.google.com')

pagetitle = driver.title

if pagetitle == 'Google':
    print("Google Homepage loaded - pass")
else:
    print("Google Homepage Not loaded - fail")

driver.quit()