import unittest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.binary_location = "C:\\Projects\\TestAutomationResources\\Python\\17. Project\\drivers\\chromedriver.exe"

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-in-process-stack-traces")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--output=/dev/null")
        
        # Hide debug logs when running in non-verbose mode
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        print(">> In method: ", self._testMethodName)
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.close()