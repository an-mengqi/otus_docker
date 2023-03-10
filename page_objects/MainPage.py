from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    CART_BUTTON = (By.ID, "cart")
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[3]/button[2]")
    ACCOUNT_DROPDOWN_MENU = (By.XPATH, "//a[contains(@href,'route=account/account')]")
    REGISTER_DROPDOWN_ITEM = (By.LINK_TEXT, "Register")
    LOGIN_DROPDOWN_ITEM = (By.LINK_TEXT, "Login")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search']/span/button")
    SEARCH_TITLE = (By.XPATH, "//*[@id='content']/h1")
    EMTY_CART_DROPDOWN_ITEM = (By.XPATH, "//*[@id='cart']/ul/li/p")
    REGISTER_ACCOUNT_TITLE = (By.XPATH, "//*[@id='content']/h1")
    CURRENCY_DROPDOWN_MENU_BUTTON = (By.XPATH, "//*[@id='form-currency']/div")
    CURRENCY_DROPDOWN_ITEM_EURO = (By.NAME, "EUR")
    CURRENCY_DROPDOWN_ITEM_POUND = (By.NAME, "GBP")
    CURRENCY_DROPDOWN_ITEM_DOLLAR = (By.NAME, "USD")
    CHOSEN_CURRENCY = (By.XPATH, "//*[@id='form-currency']/div/button/strong")
