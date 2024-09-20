from playwright.sync_api import Page, expect
from PageLib.pages import LoginPage

def test_wrong_pass(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()   
    login_page.login("standard_user", "wrong_password")
    expect(login_page.error).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service")
    