from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):

    CATALOG_MENU_OPTION = (By.ID, "menu-catalog")
    PRODUCTS_OPTION = (By.XPATH, "//*[@id='collapse1']/li[2]/a")
    CATALOG_MENU_AREA = (By.XPATH, "//*[@id='collapse1']")
    ATTRIBUTES_MENU_OPTION = (By.XPATH, "//*[@id='collapse1']/li[5]/a")
    ADD_PRODUCT_TO_LIST_BUTTON = (By.XPATH, "//*[@id='content']/div[1]/div/div/a")
    ADD_PRODUCT_PAGE_TITLE = (By.XPATH, "//*[@id='content']/div[2]/div/div[1]/h3")
    PRODUCT_NAME_FIELD = (By.ID, "input-name1")
    META_TAG_TITLE_FIELD = (By.NAME, "product_description[1][meta_title]")
    DATA_TAB = (By.XPATH, "//*[@id='form-product']/ul/li[2]/a")
    PRODUCT_MODEL_FIELD = (By.NAME, "model")
    SAVE_BUTTON = (By.XPATH, "//*[@id='content']/div[1]/div/div/button/i")
    PRODUCTS_TABLE = (By.XPATH, "//*[@id='form-product']/div/table/tbody")
    DELETE_PRODUCT_FROM_LIST_BUTTON = (By.XPATH, "//*[@id='content']/div[1]/div/div/button[3]")

    def get_menu_option_xpath(self, link):
        res = (By.XPATH, "//a[contains(@href,'route=catalog/" + link + "')]")
        return res
