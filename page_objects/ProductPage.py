from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    PRODUCT_LIST_TABLE_TITLE = (By.XPATH, "//*[@id='content']/div[2]/div/div[2]/div/div[1]/h3")
    FIRST_PRODUCT_NAME_IN_TABLE = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[1]/td[3]")
    PRODUCT_NAME_FILTER = (By.XPATH, "//*[@id='form-product']/div/table/thead/tr/td[3]/a")
    EDIT_BUTTON = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[1]/td[8]/a")
    EDIT_PRODUCT_WINDOW_TITLE = (By.XPATH, "//*[@id='content']/div[2]/div/div[1]/h3")
    FILTER_BUTTON = (By.ID, "button-filter")
    FILTER_RESULT_TEXT = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td")
    TABLE_OF_PRODUCTS = (By.XPATH, "//*[@id='form-product']/div/table/tbody")

    def get_filter_field_id(self, test_parameter):
        res = (By.ID, test_parameter)
        return res

    def get_specific_product_in_table(self, product):
        table = self.find_element(self.TABLE_OF_PRODUCTS)
        all_children_by_xpath = table.find_elements(By.XPATH, ".//tr")

        element_number = 1
        check_status = False
        for x in all_children_by_xpath:
            element_number = element_number + 1
            product_name_xpath = "//*[@id='form-product']/div/table/tbody/tr[" + str(element_number) + "]/td[3]"
            product_name = x.find_element(By.XPATH, product_name_xpath)
            if product_name.text == product:
                check_status = True
                break

        return check_status

    def get_specific_product_xpath(self, product):
        table = self.find_element(self.TABLE_OF_PRODUCTS)
        all_children_by_xpath = table.find_elements(By.XPATH, ".//tr")

        element_number = 1
        product_xpath = ''
        for x in all_children_by_xpath:
            element_number = element_number + 1
            product_name_xpath = "//*[@id='form-product']/div/table/tbody/tr[" + str(element_number) + "]/td[3]"
            product_name = x.find_element(By.XPATH, product_name_xpath)
            if product_name.text == product:
                product_xpath = "//*[@id='form-product']/div/table/tbody/tr[" + str(element_number) + "]"
                break

        return product_xpath

    def click_check_box(self, product):
        self.logger.info("Check the element {} in check-box".format(product))
        product_xpath = self.get_specific_product_xpath(product)
        check_box_xpath = product_xpath + "/td[1]/input"
        check_box_locator = (By.XPATH, check_box_xpath)
        self.click_element(check_box_locator)
