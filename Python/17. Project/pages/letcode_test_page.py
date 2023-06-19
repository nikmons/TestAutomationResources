import os 

from pages.base_page import BasePage
from locators.locators import LetCodeTestLocators, LetCodeEditLocators
from selenium.webdriver.remote.webdriver import WebDriver

class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver.get('https://letcode.in/test')
    
    def navigate_to_edit(self):
        self.click_by_xpath(LetCodeTestLocators.XP_EDIT_LINK)

    def write_full_name(self, full_name):
        full_name_el = self.find_by_xpath(LetCodeEditLocators.XP_INPUT_FULL_NAME)
        full_name_el.send_keys(full_name)
        
    def get_full_name_text(self) -> str:
        return self.find_by_xpath(LetCodeEditLocators.XP_INPUT_FULL_NAME).get_attribute("value")

    def navigate_to_click(self):
        self.click_by_xpath(LetCodeTestLocators.XP_CLICK)