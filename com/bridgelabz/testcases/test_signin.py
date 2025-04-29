
from time import sleep

import pytest
from com.bridgelabz.pageObjects.SignInPage import SignInPage
from com.bridgelabz.testcases.confitest import chrome_browser

class TestSignIn:
    url="https://bl-practice-attendance-app-stg-187791816934.asia-south1.run.app/"
    email="shaikh.shahazad@bridgelabz.com"
    password="bRidgelabz@123"

    @pytest.mark.signin
    def test_signin(self, chrome_browser):
    # chrome_browser.maximize_window()
        signin_page=SignInPage(chrome_browser)
        signin_page.open_page(self.url)
        signin_page.handle_wait(chrome_browser)
        sleep(2)

        chrome_browser.switch_to.window(chrome_browser.window_handles[1])
        sleep(1)

        signin_page.enter_email(self.email)
        signin_page.click_Next()
        sleep(2)

        signin_page.enter_password(self.password)
        sleep(2)
        signin_page.click_Next()
        sleep(2)

        chrome_browser.switch_to.window(chrome_browser.window_handles[0])

        assert "BL Practice App" in chrome_browser.title
        print("Title is",chrome_browser.title)
        sleep(10)

