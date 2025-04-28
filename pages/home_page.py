from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.search_box ="//android.widget.EditText[@resource-id='com.akakce.akakce:id/searchTextView']"


    def click_serach_button(self):
            self.click(AppiumBy.XPATH, self.search_box)  # <-- çünkü search_box XPath


