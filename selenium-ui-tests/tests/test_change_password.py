import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO: Incomplete Function.
@pytest.mark.skip(reason="Temporarily disabled")
def test_change_password(setup_browser):
    driver: WebDriver = setup_browser
    
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("Admin")
    password.send_keys("admin123")
    time.sleep(1)
    
    
    loginButton = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    loginButton.click()