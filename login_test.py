import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#@pytest.fixture
def test_login():#possitive case
    driver = webdriver.Edge()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.close()

def test_migrate_url():
    driver = webdriver.Edge()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.find_element(By.ID,"login-btn").click()
    time.sleep(3)
    driver.find_element(By.ID,"email").send_keys("poojahepzy0@gmail.com")
    driver.find_element(By.ID,"password").send_keys("Jesus4me#")
    driver.find_element(By.ID,"login-btn").click()
    actual_url = driver.current_url
    print(actual_url)
    assert "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F" == actual_url, "page not migrated"
    driver.close()

def test_incorrect_login(): #negative case
    driver = webdriver.Edge()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//button[@id='login-btn']").click()
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys("poojahepzy0@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Jesus4me")
    driver.find_element(By.ID, "login-btn").click()
    #validate error message
    time.sleep(3)
    error_text = driver.find_element(By.CLASS_NAME,"invalid-feedback").text
    print(error_text)
    assert "Incorrect Email or Password" ==error_text,"Not showing proper error message"
    driver.close()
    driver.quit() #to close browser