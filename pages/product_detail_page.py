from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.search_result_page import SearchResultsPage
class ProductDetailPage(BasePage):
    def __init__(self):
        super().__init__()

        self.go_to_seller_button = "//android.view.View[@content-desc='Satıcıya Git']/android.view.View"

    def click_go_to_product_button(self):
        search_result_page=SearchResultsPage()
        go_to_product_button=search_result_page.tenth_prodcution()
        self.click(AppiumBy.ID, go_to_product_button)

    def is_go_to_seller_button_displayed(self):
        return self.is_element_displayed(AppiumBy.ID, self.go_to_seller_button)