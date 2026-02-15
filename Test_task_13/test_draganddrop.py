from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
#launch Browser
def test_draganddrop():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    #switch iframe
    time.sleep(3)
    iframe = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
    driver.switch_to.frame(iframe)
    #drag
    draggable = driver.find_element(By.XPATH,"//div[@id='draggable']")
    #drop
    droppable = driver.find_element(By.XPATH,"//div[@id='droppable']")
    # Perform drag and drop
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()
    time.sleep(3)
    # Verify drop (check text change)
    print("Droppable text after drop:", droppable.text)
    driver.quit()

