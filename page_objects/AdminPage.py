import allure

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):

    USERNAME_INPUT_FIELD = (By.NAME, "username")
    PASSWORD_INPUT_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i")
    AUTH_WINDOW = (By.XPATH, "//div[@class='panel panel-default']")
    FORGOTTEN_PASSWORD_LINK = (By.XPATH, "//a[contains(@href,'route=common/forgotten')]")
    FORGOT_PASSWORD_WINDOW_TITLE = (By.XPATH, "//*[@id='content']/div/div/div/div/div[1]/h1")
    DASHBOARD_PAGE_TITLE = (By.XPATH, "//*[@id='content']/div[1]/div/h1")

    def login(self, user_name, user_password):
        self.logger.info("Login as: {}".format(user_name))
        with allure.step(f'Ввожу логин: {user_name}'):
            self.input_value(self.USERNAME_INPUT_FIELD, user_name)

        with allure.step(f'Ввожу пароль: {user_password}'):
            self.input_value(self.PASSWORD_INPUT_FIELD, user_password)

        with allure.step("Нажимаю на кнопку Login"):
            self.click_element(self.LOGIN_BUTTON)
        return self
    