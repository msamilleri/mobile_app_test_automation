from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class NotificationSkip(BasePage):
    def __init__(self):
        super().__init__()
        self.dont_allow = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"

    def notification_dont_allow(self):
        self.driver.find_element(AppiumBy.XPATH, self.dont_allow).click()

    def dont_allow(self):
        try:
            self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button").click()
        except:
            print("Don't allow button not found or already handled")












