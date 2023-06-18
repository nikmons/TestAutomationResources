import sys
import os
import unittest
import time

from tests.base_test import BaseTest

base_dir = os.path.dirname(__file__) or '.'
sys.path.append("..")

from pages.letcode_test_page import HomePage

class FTestLetCodeEditPage(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)

    def test_navigate_to_edit(self):
        self.home_page.navigate_to_edit()

        assert self.driver.current_url == "https://letcode.in/edit"

        #time.sleep(10)

        full_name_val = "Mitsos Mitsou"
        self.home_page.write_full_name(full_name_val)
        
        time.sleep(3)
        
        assert self.home_page.get_full_name_text() == full_name_val

    def test_navigate_to_click(self):
        self.home_page.navigate_to_click()

        assert self.driver.current_url == "https://letcode.in/buttons"
    
if __name__ == "__main__":
    unittest.main(warnings='ignore')