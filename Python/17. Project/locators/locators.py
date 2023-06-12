from selenium.webdriver.common.by import By

class LetCodeTestLocators():
    lc_edit_link = (By.XPATH, "//a[.='Edit']")
    lc_click = (By.XPATH, "//a[.='Click']")
    lc_drop_down = (By.XPATH, " //a[.='Drop-Down']")
    lc_alert = (By.XPATH, " //a[.='Dialog']")

    lc_inner_html = (By.XPATH, "//a[.='Inner HTML']")
    lc_toggle = (By.XPATH, "//a[.='Toggle']")
    lc_tabs = (By.XPATH, "//a[.='Tabs']")
    lc_find_elements = (By.XPATH, "//a[.='Find Elements']")

    lc_drag = (By.XPATH, "drag //a[.='AUI - 1']")
    lc_drop = (By.XPATH, "drop //a[.='AUI - 2']")
    lc_sort = (By.XPATH, "sort //a[.='AUI - 3']")
    lc_nulti_select = (By.XPATH, "multi_select //a[.='AUI - 4']")

    lc_slider = (By.XPATH, "slider //a[.='AUI - 5']")
    lc_tables_simple = (By.XPATH, "table_simple //a[.='Simple table']")
    lc_tables_advanced = (By.XPATH, "table_advanced //a[.='Advance table']")
    lc_calendar = (By.XPATH, "datetime //a[.='Date & Time']")

    lc_wait = (By.XPATH, "wait //a[.='Timeout']")
    lc_form = (By.XPATH, "form //a[.='All in One']")
    lc_files = (By.XPATH, "files //a[.='File management']")
    lc_shadow = (By.XPATH, "shadow //a[.='DOM']")
    lc_snake_game = (By.XPATH, "snake_game //a[.='Play it!']")

class LetCodeEditLocators():
    lc_input_full_name = (By.XPATH, "//input[@id='fullName']")

class HomePageLocators():
    yt_search_field = (By.ID, "search")
    yt_search_button = (By.CLASS_NAME, "style-scope ytd-searchbox")