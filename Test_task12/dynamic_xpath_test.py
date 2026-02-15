import time
from selenium.webdriver.common.by import By

def test_option1(launch_guvi):
    driver = launch_guvi
    time.sleep(3)
    parent = driver.find_element(By.XPATH,"//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'][normalize-space()='LIVE Classes']").click()
    print(parent)
    child = driver.find_element(By.XPATH,"//p[normalize-space()='Software Development']").text
    print(child)
