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
def test_option2(launch_guvi):
    driver = launch_guvi
    first_elem = driver.find_element(By.XPATH, "//div[@id='solutions']/child::p[.='Courses']")
    first_elem.click()
    text_first_elem = first_elem.text
    print("\nThe identified Element is ", text_first_elem)
    first_child = driver.find_element(By.XPATH, "//div[@class='⭐️f6lmuc-0 flex items-center gap-2 w-full p-2 drop-content lg:min-w-60 cursor-pointer']/child::p[.='Free Courses']").text
    print("\nFirst child for the element ", text_first_elem, "is ", first_child)
    print("\n There is no sibling associated with the Element")
    print("All children associated with the Element")
    all_child_list = driver.find_elements(By.XPATH, "//div[@class='⭐️f6lmuc-0 flex flex-col p-4 gap-1 contents-container']/child::div/child::p")
    all_text = []
    for child in all_child_list:
        text = child.text
        all_text.append(text)
        print(text)
    driver.close()

def test_option3(launch_guvi):
    driver = launch_guvi
    first_elem = driver.find_element(By.XPATH,"//div[@id='solutions']/child::p[.='Practice']")
    first_elem.click()
    text_first_elem = first_elem.text
    print("\nThe identified Element is ",text_first_elem)
    first_child = driver.find_element(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex flex-col justify-center']/child::p[text()='CodeKata']").text
    print("\nFirst child for the element ",text_first_elem ,"is ",first_child)
    #sibling
    sibling = driver.find_element(By.XPATH,"//p[contains(text(),'Sharpen your coding skills, prepare for interviews')]").text
    print("Sibling is ",sibling)
    #fetching all Children
    print("All children associated with the Element")
    all_child_list = driver.find_elements(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex items-center gap-2 w-full p-2 drop-content cursor-pointer']//child::p[1]")
    all_text = []
    for child in all_child_list:
        text = child.text
        all_text.append(text)
        print(text)
    driver.close()

def test_option4(launch_guvi):
    driver = launch_guvi
    first_elem = driver.find_element(By.XPATH,"//div[@id='solutions']/child::p[.='Resources']")
    first_elem.click()
    text_first_elem = first_elem.text
    print("\nThe identified Element is ", text_first_elem)
    first_child = driver.find_element(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex items-center gap-2 w-full p-2 drop-content lg:min-w-60 cursor-pointer']/child::p[text()='Free Resources']").text
    print("\nFirst child for the element ", text_first_elem, "is ", first_child)
    # sibling
    print("There is no siblings associated with the Elements")
    # fetching all Children
    print("All children associated with the Element")
    all_child_list = driver.find_elements(By.XPATH,"//div[@class='⭐️f6lmuc-0 px-5 grid grid-cols-2 gap-x-2 gap-y-1 w-max']//child::p")
    all_text = []
    for child in all_child_list:
        text = child.text
        all_text.append(text)
        print(text)
    driver.close()

def test_option5(launch_guvi):
    driver = launch_guvi
    driver = launch_guvi
    first_elem = driver.find_element(By.XPATH, "//div[@id='solutions']/child::p[.='Our Products']")
    first_elem.click()
    text_first_elem = first_elem.text
    print("\nThe identified Element is ", text_first_elem)
    first_child = driver.find_element(By.XPATH, "//div[@class='⭐️f6lmuc-0 flex flex-col justify-center']/child::p[.='HackerKID']").text
    print("\nFirst child for the element ", text_first_elem, "is ", first_child)
    # sibling
    sibling = driver.find_element(By.XPATH, "(//div[@class='⭐️f6lmuc-0 flex items-center gap-2 p-2 drop-content cursor-pointer']//child::p[2])[1]").text
    print("Sibling is ", sibling)
    # fetching all Children
    print("All children associated with the Element")
    all_child_list = driver.find_elements(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex items-center gap-2 p-2 drop-content cursor-pointer']//child::p[1]")
    all_text = []
    for child in all_child_list:
        text = child.text
        all_text.append(text)
        print(text)
    driver.close()

