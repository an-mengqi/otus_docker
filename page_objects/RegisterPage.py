from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    LOGIN_PAGE_LINK = (By.XPATH, "//*[@id='content']/p/a")
    BREADCRUMB_LOGIN_TAB = (By.XPATH, "//*[@id='account-login']/ul/li[3]/a")
    SUBSCRIBE_RADIO_BUTTON_NO = (By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[2]/input")
    FIRSTNAME_FIELD = (By.NAME, "firstname")
    LASTNAME_FIELD = (By.NAME, "lastname")
    EMAIL_FIELD = (By.NAME, "email")
    TELEPHONE_FIELD = (By.NAME, "telephone")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "confirm")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='content']/form/div/div/input[2]")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//*[@id='content']/form/div/div/input[1]")
    REGISTER_SUCCESS_PAGE_TITLE = (By.XPATH, "//*[@id='content']/h1")

    def get_personal_details_fields_xpath(self, element_number):
        res = (By.XPATH, "//*[@id='account']/div[" + element_number + "]/label")
        return res

    def get_password_fields_xpath(self, element_number):
        res = (By.XPATH, "//*[@id='content']/form/fieldset[2]/div[" + element_number + "]/label")
        return res
