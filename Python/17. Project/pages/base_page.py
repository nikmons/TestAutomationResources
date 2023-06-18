from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage():
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def __init__(self, driver: WebDriver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver
    
    def click_by_xpath(self, by_locator: str):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).click()
    
    def find_by_xpath(self, by_locator: str):
        return self.driver.find_element(By.XPATH, by_locator)