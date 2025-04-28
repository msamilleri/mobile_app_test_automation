from appium import webdriver
from appium.options.android import UiAutomator2Options


class DriverManager:
    driver = None

    @staticmethod
    def get_driver():
        if DriverManager.driver is None:
            DriverManager.init_driver()
        return DriverManager.driver




    @staticmethod
    def init_driver():
        options = UiAutomator2Options()
        options.set_capability('platformName', 'Android')
        options.set_capability('appium:deviceName', 'Pixel 4 API 36')
        options.set_capability('appium:automationName', 'UiAutomator2')
        options.set_capability('appium:appPackage', 'com.akakce.akakce')
        options.set_capability('appium:appActivity', 'com.akakce.akakce.ui.splash.SplashActivity')
        options.set_capability('appium:noReset', False)
        options.set_capability('appium:skipUnlock', True)
        DriverManager.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        DriverManager.driver.implicitly_wait(15)
        return DriverManager.driver

    @staticmethod
    def close_driver():
        if DriverManager.driver:
            DriverManager.driver.quit()
            DriverManager.driver = None