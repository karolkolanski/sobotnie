from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.google.pl")
pole_wyszukiwania = driver.find_element_by_name('q')
pole_wyszukiwania.send_keys("tester cdv")
time.sleep(1)
pole_wyszukiwania.clear()
pole_wyszukiwania.submit()
time.sleep(2)
driver.close()

