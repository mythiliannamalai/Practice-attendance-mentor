import os
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
        act_title=chrome_browser.title
        if act_title == "BL Practice App123":
            assert True
        else:
            # time.sleep(2)
            if not os.path.exists("C:\\Users\\Admin\\PycharmProjects\\BridgelabzAttedanceSystem\\com\\bridgelabz\\ScreenShots"):
                os.makedirs("./ScreenShots")

            chrome_browser.save_screenshot(
                "C:\\Users\\Admin\\PycharmProjects\\BridgelabzAttedanceSystem\\com\\bridgelabz\\ScreenShots\\test_signin.png")
            assert False, f"Title mismatch: Expected 'BL Practice App', got '{act_title}'"
        print("Title is",chrome_browser.title)
        sleep(10)

