from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")  
        self.password = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.title = page.locator("[data-test=\"title\"]")
        self.error = page.locator("[data-test=\"error\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_sort = page.locator("[data-test=\"product-sort-container\"]")
        self.inventory_list = page.locator("[data-test=\"inventory-list\"]")
        self.items_price = page.locator("[data-test=\"inventory-item-price\"]")
        self.add_to_cart_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.shopping_cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def sort(self, option):
        self.product_sort.select_option(option)
    
    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def open_cart(self):
        self.shopping_cart_link.click()


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_list = page.locator("[data-test=\"cart-list\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")

    def checkout(self):
        self.checkout_button.click()


class CheckoutStepOne:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")

    def information(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()


class CheckoutStepTwo:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator("[data-test=\"finish\"]")

    def finish(self):
        self.finish_button.click()


class CheckoutComplete:
    def __init__(self, page: Page):
        self.page = page
        self.complete_header = page.locator("[data-test=\"complete-header\"]")
