from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    def __init__(self):
        super().__init__()
        self.go_to_product_button = "com.akakce.akakce:id/goToProductButton"
        self.go_to_seller_button = "com.akakce.akakce:id/goToSellerButton"

    def click_go_to_product_button(self):
        self.click(AppiumBy.ID, self.go_to_product_button)

    def is_go_to_seller_button_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.go_to_seller_button)