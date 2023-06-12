from pages.base_page import BasePage
from locators.locators import LetCodeTestLocators, LetCodeEditLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://letcode.in/test')
    
    def navigate_to_edit(self):
        self.click(LetCodeTestLocators.lc_edit_link)

    def write_full_name(self, full_name):
        full_name_el = self.find(LetCodeEditLocators.lc_input_full_name)

    def navigate_to_click(self):
        self.click(LetCodeTestLocators.lc_click)