class MainPageLocators():
    LOGIN_LINK = ('css selector','#login_link')

class LoginPageLocators():
    login_form = ('css selector', "#login_form")
    register_form =('css selector', "#register_form")

class ProductPageLocators():
    button = ('css selector', '.btn.btn-lg.btn-primary')
    price_one = ('css selector', '.alertinner p strong')
    price_two = ('css selector', '.col-sm-6.product_main .price_color')
    name_one = ('css selector', '.alertinner strong')
    name_two = ('css selector', '.col-sm-6.product_main h1')
    success_massage = ('css selector', '#messages div:nth-child(1)')

class BasePageLocators():
    LOGIN_LINK = ('css selector', "#login_link")
    LOGIN_LINK_INVALID = ('css selector', "#login_link_inc")