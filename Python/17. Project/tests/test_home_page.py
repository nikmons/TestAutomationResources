# import sys
# import os
# import unittest

# from tests.base_test import BaseTest

# base_dir = os.path.dirname(__file__) or '.'
# sys.path.append("..")

# from pages.yt_home_page import HomePage

# class FTestYTHomePage(BaseTest):
#     def setUp(self):
#         super().setUp()
#         self.home_page = HomePage(self.driver)

#     def test_search_video(self):
#         self.home_page.search_video("Python Tutorial")
    
# if __name__ == "__main__":
#     unittest.main()