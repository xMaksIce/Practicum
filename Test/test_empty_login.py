from playwright.sync_api import Page, expect
from PageLib.pages import LoginPage

def test_empty_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()   
    login_page.login("", "")
    expect(login_page.error).to_contain_text(
        "Epic sadface: Username is required")
