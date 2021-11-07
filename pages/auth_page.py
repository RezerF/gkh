from .base_page import BasePage
from .locators import AuthPageLocators
import constants


class AuthPage(BasePage):
    def __init__(self, driver, url):
        # super.__init__(driver, url)
        super().__init__(driver, url)

    URL = ""
    def login_insert(self):
        self.driver.find_element(*AuthPageLocators.LOGIN).send_keys(constants.LOGIN)

    def pass_insert(self):
        self.driver.find_element(*AuthPageLocators.PASS).send_keys(constants.PASS)

    def submit_button_click(self):
        self.driver.find_element(*AuthPageLocators.SUBMIT_BUTTON).click()

    def authorize(self):
        self.login_insert()
        self.pass_insert()
        self.submit_button_click()
