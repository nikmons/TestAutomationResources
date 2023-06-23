from selenium.webdriver.common.by import By

# test landing screen locators 
class LetCodeTestLocators():
    XP_EDIT_LINK: str = "//a[.='Edit']"
    XP_CLICK: str = "//a[.='Click']"
    XP_DROP_DOWN: str = " //a[.='Drop-Down']"
    XP_ALERT: str = " //a[.='Dialog']"

    XP_INNER_HTML: str = "//a[.='Inner HTML']"
    XP_TOGGLE: str = "//a[.='Toggle']"
    XP_TABS: str = "//a[.='Tabs']"
    XP_FIND_ELEMENTS: str = "//a[.='Find Elements']"

    XP_DRAG: str = "drag //a[.='AUI - 1']"
    XP_DROP: str = "drop //a[.='AUI - 2']"
    XP_SORT: str = "sort //a[.='AUI - 3']"
    XP_MULTI_SELECT: str = "multi_select //a[.='AUI - 4']"

    XP_SLIDER: str = "slider //a[.='AUI - 5']"
    XP_TABLES_SIMPLE: str = "table_simple //a[.='Simple table']"
    XP_TABLES_ADVANCED: str = "table_advanced //a[.='Advance table']"
    XP_CALENDAR: str = "datetime //a[.='Date & Time']"

    XP_WAIT: str = "wait //a[.='Timeout']"
    XP_FORM: str = "form //a[.='All in One']"
    XP_FILES: str = "files //a[.='File management']"
    XP_SHADOW: str = "shadow //a[.='DOM']"
    XP_SNAKE_GAME: str = "snake_game //a[.='Play it!']"

# edit screen locators
class LetCodeEditLocators():
    XP_INPUT_FULL_NAME: str = "//input[@id='fullName']"
    XP_APPEND: str = "//input[@id='join']"
    XP_READ: str = "//input[@id='getMe']"
    XP_CLEAR: str = "//input[@id='clearMe']"
    XP_DISABLED: str = "//input[@id='noEdit']"
    XP_READ_ONLY: str = "//input[@id='dontwrite']"

class HomePageLocators():
    yt_search_field: By = (By.ID, "search")
    yt_search_button: By = (By.CLASS_NAME, "style-scope ytd-searchbox")