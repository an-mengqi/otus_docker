import allure

from page_objects.AdminPage import AdminPage

@allure.step("Ищу окно с формой авторизации")
def test_login_window(browser):
    """Check that there is a login window on the page"""
    assert AdminPage(browser).find_element(AdminPage.AUTH_WINDOW)
