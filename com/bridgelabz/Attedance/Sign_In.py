#
# import time
#
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from com.tests.confitest import chrome_browser
#
# def test_signin(chrome_browser):
#     chrome_browser.get("https://bl-practice-attendance-app-stg-187791816934.asia-south1.run.app/")
#     chrome_browser.maximize_window()
#     #
#     wait = WebDriverWait(chrome_browser, 200)
#     sign_in_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Sign in with Google')]")))
#     sign_in_button.click()
#     print("Clicked on 'Sign in with Google' successfully!")
#     sleep(2)
#     chrome_browser.switch_to.window(chrome_browser.window_handles[1])
#     sleep(1)
#     email_textbox = chrome_browser.find_element(By.XPATH, '//input[@type="email"]')
#     email_textbox.send_keys("shaikh.shahazad@bridgelabz.com")
#     chrome_browser.find_element(By.XPATH, '//span[text()="Next"]').click()
#     sleep(2)
#     password_input = chrome_browser.find_element(By.XPATH, '//input[@type="password"]')
#     password_input.click()
#     password_input.send_keys("bRidgelabz@123" + Keys.TAB)
#     sleep(2)
#     chrome_browser.find_element(By.XPATH, '//span[text()="Next"]').click()
#     sleep(2)
#     chrome_browser.switch_to.window(chrome_browser.window_handles[0])
#     sleep(10)
#
