from playwright.sync_api import Page, expect
from PageLib.pages import LoginPage, ProductsPage, CartPage

def test_add_item(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    login_page.navigate()   
    login_page.login("standard_user", "secret_sauce")
    products_page.add_backpack_to_cart()
    expect(products_page.shopping_cart_badge).to_have_count(1)
    products_page.open_cart()
    expect(cart_page.cart_list).to_contain_text("Sauce Labs Backpack")
