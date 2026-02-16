import time
from selenium.webdriver.common.by import By

def test_option1(launch_guvi):
    driver = launch_guvi
    first_elem = driver.find_element(By.XPATH,"//div[@id='solutions']/child::p[.='LIVE Classes']").click()
   # print("The identified Element is ",first_elem)
    first_child = driver.find_element(By.XPATH,"(//div[@class='⭐️f6lmuc-0 flex items-center gap-2']/child::p)[1]").text
    print("\nFirst child for the element LIVE Classes is ",first_child)
    sibling = driver.find_element(By.XPATH,"//p[.='Software Development ']/following-sibling::span").text
    print("Sibling is ",sibling)
    print("All children associated with the Element")
    all_children = driver.find_elements(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex items-center gap-2']/child::p")
    for child in all_children:
        all= driver.find_element(child).text
        print(all)
    driver.close()