from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.skip_login_button = "//android.widget.RelativeLayout[@resource-id='com.akakce.akakce:id/inner_cell']"

    def skip_login(self):
        self.driver.find_element(AppiumBy.XPATH, self.skip_login_button).click()














