
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bl-practice-attendance-app-stg-187791816934.asia-south1.run.app/")
driver.maximize_window()

# Now, try finding and clicking the element

wait = WebDriverWait(driver, 200)
sign_in_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Sign in with Google')]")))
sign_in_button.click()
print("Clicked on 'Sign in with Google' successfully!")
sleep(2)
driver.switch_to.window(driver.window_handles[1])
sleep(1)
email_textbox = driver.find_element(By.XPATH, '//input[@type="email"]')
email_textbox.send_keys("shaikh.shahazad@bridgelabz.com")
# email_textbox.submit()
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
sleep(3)
driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("bRidgelabz@123")
sleep(3)
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
sleep(3)

driver.switch_to.window(driver.window_handles[0])
# sleep(10)

wait = WebDriverWait(driver, 200)
delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='disable']")))
delete_button.click()

wait = WebDriverWait(driver, 200)
time.sleep(3)
# Wait for the button with visible text 'Yes, Disable'
yes_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[normalize-space()='Yes, Disable']")
))
time.sleep(1)
# Use JavaScript click to avoid overlay/interception
driver.execute_script("arguments[0].click();", yes_button)

# disable_button.click()
time.sleep(3)