
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

wait = WebDriverWait(driver, 10)
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='edit']")))
edit_button.click()


lab_name_input = driver.find_element(By.NAME, "labName")
new_value = "Bridge Lab12"

driver.execute_script("""
  const input = arguments[0];
  const newValue = arguments[1];
  const lastValue = input.value;

  input.value = newValue;

  const event = new Event('input', { bubbles: true });
  event.simulated = true;

  const tracker = input._valueTracker;
  if (tracker) {
    tracker.setValue(lastValue);
  }

  input.dispatchEvent(event);
""", lab_name_input, new_value)
time.sleep(2)


# Update a time
wait = WebDriverWait(driver, 10)
start_time_input=wait.until(EC.element_to_be_clickable((By.NAME, "startTime")))
start_time_input.send_keys("08:00")

wait = WebDriverWait(driver, 10)
end_time_input=wait.until(EC.element_to_be_clickable((By.NAME, "endTime")))
end_time_input.send_keys("21:00")

time.sleep(2)

# Update the Radio Button
wait = WebDriverWait(driver, 20)

# Get the label element containing the radio with value='Fellowship'
fellowship_radio_label = wait.until(EC.presence_of_element_located((
    By.XPATH,
    "//input[@type='radio' and @value='Fellowship']/parent::span"
)))

# Use ActionChains to click it
actions = ActionChains(driver)
actions.move_to_element(fellowship_radio_label).click().perform()

print("✅ Fellowship radio selected.")

wait = WebDriverWait(driver, 30)
updated_lab =  wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']")))
updated_lab.click()

time.sleep(2)