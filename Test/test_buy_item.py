from playwright.sync_api import Page, expect
from PageLib.pages import LoginPage, ProductsPage, CartPage, CheckoutStepOne, CheckoutStepTwo, CheckoutComplete

def test_buy_item(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkoutStepOne = CheckoutStepOne(page)
    checkoutStepTwo = CheckoutStepTwo(page)
    checkoutComplete = CheckoutComplete(page)
    login_page.navigate()   
    login_page.login("standard_user", "secret_sauce")
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.checkout()
    checkoutStepOne.information("John", "Doe", "404")
    checkoutStepTwo.finish()
    expect(checkoutComplete.complete_header).to_be_visible()
