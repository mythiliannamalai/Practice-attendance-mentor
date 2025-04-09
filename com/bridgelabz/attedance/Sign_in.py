
import time

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
sleep(2)
driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("bRidgelabz@123")
sleep(2)
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
sleep(2)
driver.switch_to.window(driver.window_handles[0])
sleep(10)

#
# wait = WebDriverWait(driver, 10)
# create_lab = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="CREATE LAB"]')))
# create_lab.click()
# sleep(3)
#
# wait = WebDriverWait(driver, 10)
# dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='COE']/following::div[@role='combobox'][1]")))
# dropdown.click()
#
#
# option = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul//li[contains(text(),'Bombay Quality K')]")))
#
# # Scroll it into view
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
# time.sleep(2)
#
# driver.execute_script("arguments[0].click();", option)
# print("DropDown Selection succ")
#
# # Create a Lab Name
# driver.find_element(By.NAME, "labName").send_keys("Lab Five")
# time.sleep(2)
#
# # Create a time
# wait = WebDriverWait(driver, 10)
# start_time_input=wait.until(EC.element_to_be_clickable((By.NAME, "startTime")))
# start_time_input.send_keys("10:00")
#
# wait = WebDriverWait(driver, 10)
# end_time_input=wait.until(EC.element_to_be_clickable((By.NAME, "endTime")))
# end_time_input.send_keys("19:00")
#
# print("Time selected successfully")
#
# wait=WebDriverWait(driver, 10)
# # Click the visible element associated with the radio input
# radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='CodinClub']/parent::span")))
# radio.click()
#
# wait = WebDriverWait(driver, 10)
# created_lab =  wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create']")))
# created_lab.click()
#
# time.sleep(2)
#
# # driver.switch_to.window(driver.window_handles[1])
#
# wait = WebDriverWait(driver, 10)
# edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='edit']")))
# edit_button.click()
#
# time.sleep(3)