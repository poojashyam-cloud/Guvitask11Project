from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.chrome()
driver.get("https://www.guvi.in/")
driver.maximize_window()
driver.get_elements
