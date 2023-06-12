# from pages.base_page import BasePage
# from locators.locators import HomePageLocators

# class HomePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver.get('http://www.youtube.com')
    
#     def search_video(self, video_text):
#         self.enter_text(HomePageLocators.yt_search_field, video_text)
#         self.click(HomePageLocators.yt_search_button)