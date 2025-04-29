from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage:
    sign_login_xpath= "//span[contains(text(),'Sign in with Google')]"
    email_xpath='//input[@type="email"]'
    password_xpath='//input[@type="password"]'
    next_button_xpath='//span[text()="Next"]'

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def handle_wait(self, driver):
        wait = WebDriverWait(driver, 200)
        sign_in_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.sign_login_xpath)))
        sign_in_button.click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def enter_password(self, password):
        password_input=self.driver.find_element(By.XPATH,self.password_xpath )
        password_input.click()
        password_input.send_keys(password + Keys.TAB)

    def click_Next(self):
        self.driver.find_element(By.XPATH,self.next_button_xpath).click()
