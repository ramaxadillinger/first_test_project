from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()



def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ "
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.is_element_present(By.CSS_SELECTOR, "#login_link")


def test_1(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/accounts/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
