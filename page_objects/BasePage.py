import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Did not wait for the element to be visible: {locator}")

    def input_value(self, locator, value):
        """Input value in a field"""
        self.logger.info("Input {} in input {}".format(value, locator))
        self.element(locator).send_keys(value)

    def click_element(self, locator):
        """Click on the element"""
        self.logger.info("Clicking element: {}".format(locator))
        self.element(locator).click()

    def find_element(self, locator):
        return self.element(locator)

    def get_element_text(self, locator):
        self.logger.info("Finding element {} text".format(locator))
        element = self.find_element(locator)
        return element.text

    def get_element_attribute(self, locator, attribute):
        self.logger.info("Finding attribute {} in element {}".format(attribute, locator))
        return self.find_element(locator).get_attribute(attribute)
