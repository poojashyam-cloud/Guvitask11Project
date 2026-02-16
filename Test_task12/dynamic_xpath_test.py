import time
from selenium.webdriver.common.by import By

def test_option1(launch_guvi):
    driver = launch_guvi
    first_elem = driver.find_element(By.XPATH,"//div[@id='solutions']/child::p[.='LIVE Classes']")
    first_elem.click()
    text_first_elem = first_elem.text
    print("\nThe identified Element is ",text_first_elem)
    first_child = driver.find_element(By.XPATH,"(//div[@class='⭐️f6lmuc-0 flex items-center gap-2']/child::p)[1]").text
    print("\nFirst child for the element ",text_first_elem ,"is ",first_child)
    #sibling
    sibling = driver.find_element(By.XPATH,"//p[.='Software Development ']/following-sibling::span").text
    print("Sibling is ",sibling)
    #fetching all Children
    print("All children associated with the Element")
    all_child_list = driver.find_elements(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex items-center gap-2']/child::p")
    all_text = []
    for child in all_child_list:
        text = child.text
        all_text.append(text)
        print(text)
    driver.close()