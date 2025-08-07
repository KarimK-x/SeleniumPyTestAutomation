import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login(setup_browser):
    """
    Test Case ID: Login_02
    Validates failure to login with incorrect credentials
    """
    
    driver: WebDriver = setup_browser
    driver.get(url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("wrongUser")
    password.send_keys("wrongPass")
    
    loginButton = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    loginButton.click()
    
    try:
        invalidLogin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]"))
            )
        # print(invalidLogin.text)
        assert invalidLogin.text == "Invalid credentials", f"Expected error message to say \"Invalid Credentials\". Got {invalidLogin.text}"
        print("Invalid Login Test Passed!")
    except:
        assert False, "Invalid Login Test Failed!"
    time.sleep(2)
    
def test_valid_login(setup_browser):
    """
    Test Case ID: Login_01
    Validates successful login with correct credentials
    """
    driver: WebDriver = setup_browser
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("Admin")
    password.send_keys("admin123")
    time.sleep(1)
    
    loginButton = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    loginButton.click()
    
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/dashboard")
            )
        assert "/dashboard" in driver.current_url, f"Expected dashboard URL, got: {driver.current_url}"
        print("Valid Login Test Passed!")
    except:
        assert False, "Invalid Login"
        
    
    
        
    
    

    

    
     
        

    
    
    
