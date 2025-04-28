from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class FilterPage(BasePage):
    def __init__(self):
        super().__init__()
        self.category_computer_hardware = "//android.widget.TextView[contains(@text, 'Bilgisayar,Donanım')]"
        self.show_products_button = "com.akakce.akakce:id/showProductsButton"

    def select_computer_hardware_category(self):
        self.click(AppiumBy.XPATH, self.category_computer_hardware)

    def click_show_products_button(self):
        self.click(AppiumBy.ID, self.show_products_button)