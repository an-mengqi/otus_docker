from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SuccessAlert(BasePage):

    SUCCESS_ALERT = (By.XPATH, "//*[@id='common-home']/div[1]")
    REGISTER_WARNING_ALERT = (By.XPATH, "//*[@id='account-register']/div[1]")
    PRODUCT_MODIFIED_ALERT = (By.XPATH, "//*[@id='content']/div[2]/div[1]")
