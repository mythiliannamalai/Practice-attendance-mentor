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
# driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("bRidgelabz@123")
password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
password_input.click()
password_input.send_keys("bRidgelabz@123" + Keys.TAB)

sleep(2)
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
sleep(2)
driver.switch_to.window(driver.window_handles[0])
sleep(10)
#
# wait = WebDriverWait(driver, 10)
#
# Wait and click on the Daily Practice tab in the sidebar
daily_practice_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Daily Practice']")))
driver.execute_script("arguments[0].click();", daily_practice_tab)
# sleep(3)


# Click the item
# driver.find_element(By.XPATH, "//span[text()='Daily Practice']").click()
print("Daily Practice page opens")
time.sleep(2)

wait = WebDriverWait(driver, 10)
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='COE']/following::div[@role='combobox'][1]")))
dropdown.click()

option = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul//li[contains(text(),'Bombay Quality K')]")))

# Scroll it into view
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
time.sleep(2)

driver.execute_script("arguments[0].click();", option)

# Select Lab
wait=WebDriverWait(driver, 10)
lab_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Lab Name']/following::div[@role='combobox'][1]")))
lab_dropdown.click()
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul//li[contains(text(),'Bombay Lab 1')]")))

driver.execute_script("arguments[0].click();", option)

wait = WebDriverWait(driver, 20)
view_lab = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'VIEW')]")
))

view_lab.click()
time.sleep(2)


wait = WebDriverWait(driver, 200)
download_qr_practice_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Download QR']")))
download_qr_practice_button.click()
# driver.execute_script("arguments[0].click();", view_lab)
time.sleep(3)
