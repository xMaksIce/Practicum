from playwright.sync_api import Page
from PageLib.pages import LoginPage, ProductsPage

def test_sorted_items(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    login_page.navigate()   
    login_page.login("standard_user", "secret_sauce")
    prev_price = -1
    products_page.sort("lohi")
    for i in range(products_page.items_price.count()):
        price_text = products_page.items_price.nth(i).inner_text()
        price_value = float(price_text.replace("$", ""))
        assert prev_price <= price_value
        prev_price = price_value
