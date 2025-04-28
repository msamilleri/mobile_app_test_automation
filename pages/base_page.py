from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utilities.driversManager import DriverManager

class BasePage:
    def __init__(self):
        self.driver = DriverManager.get_driver()
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_element_visible(self, locator_strategy, locator):
        return self.wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

    def wait_for_element_clickable(self, locator_strategy, locator):
        return self.wait.until(EC.element_to_be_clickable((locator_strategy, locator)))

    def click(self, locator_strategy, locator):
        element = self.wait_for_element_clickable(locator_strategy, locator)
        element.click()

    def send_keys(self, locator_strategy, locator, text):
        element = self.wait_for_element_visible(locator_strategy, locator)
        element.send_keys(text)

    def get_text(self, locator_strategy, locator):
        element = self.wait_for_element_visible(locator_strategy, locator)
        return element.text

    def is_element_displayed(self, locator_strategy, locator):
        try:
            return self.driver.find_element(locator_strategy, locator).is_displayed()
        except NoSuchElementException:
            return False

    def find_element_by_index(self, locator_strategy, locator, index):
        elements = self.driver.find_elements(locator_strategy, locator)
        if 0 <= index < len(elements):
            return elements[index]
        else:
            raise IndexError(f"Element bulunamadı, index: {index}")