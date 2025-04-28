
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self):
        super().__init__()
        self.search_box = "(//android.widget.EditText[@resource-id='com.akakce.akakce:id/searchTextView'])[2]" # XPath
        self.search_laptop = "//android.widget.TextView[@resource-id='com.akakce.akakce:id/textView' and @text='Laptop ve Notebook']" # XPath


    # Find the search boc and write 'Laptop'
    def search_product(self, product):
        self.wait_for_element_visible(AppiumBy.XPATH, self.search_box)
        self.click(AppiumBy.XPATH, self.search_box)
        self.send_keys(AppiumBy.XPATH, self.search_box, product)
        self.click(AppiumBy.XPATH, self.search_laptop)











