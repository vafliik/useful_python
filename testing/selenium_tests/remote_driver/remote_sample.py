"""
Very simple example of Remote Webdriver test
"""

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

driver.get('http://www.javascripting.com')

driver.quit()
