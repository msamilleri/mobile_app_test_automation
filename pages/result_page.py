import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pages.base_page import BasePage
from utilities.driversManager import DriverManager
driver=DriverManager.get_driver()
class ResultPage(BasePage):
    def __init__(self):
        super().__init__()
        self.selecet_all_button = "(//android.widget.TextView[@resource-id='com.akakce.akakce:id/hplAllTv'])[2]"
        self.selecet_filtre_buton = "//android.widget.TextView[@resource-id='com.akakce.akakce:id/selectedSortText']"

        self.selecet_highest_price= "//android.widget.TextView[@resource-id='com.akakce.akakce:id/sort_name' and @text='En Yüksek Fiyat']"

    def push_filtre_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.selecet_filtre_buton).click()

    def push_highest_price_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.selecet_highest_price).click()

    def click_show_products_button(self):
        #Appium record,
        try:
            push_all_product_button = self.wait_for_element_visible(AppiumBy.ANDROID_UIAUTOMATOR,
                                                'new UiSelector().resourceId("com.akakce.akakce:id/hplAllTv").instance(1)')
            push_all_product_button.click()
            push_all_product_button.click()
        except Exception as e:
            print("ERROR: push_all_product_button not found", str(e))

        try:
            push_filtrele_button= self.wait_for_element_visible(AppiumBy.ANDROID_UIAUTOMATOR,
                                                'new UiSelector().text("Filtrele")')
            push_filtrele_button.click()
        except Exception as e:
            print("ERROR: push_filtrele_button (Filtrele) not found", str(e))

        try:
            push_bilgisayar_donanim_button = self.wait_for_element_visible(AppiumBy.ANDROID_UIAUTOMATOR,
                                                'new UiSelector().text("Bilgisayar, Donanım")')
            push_bilgisayar_donanim_button.click()
        except Exception as e:
            print("ERROR: push_bilgisayar_donanim_button (Bilgisayar, Donanım) not found", str(e))

        try:
            push_return_result_page_button = self.wait_for_element_visible(AppiumBy.ANDROID_UIAUTOMATOR,
                                                'new UiSelector().resourceId("com.akakce.akakce:id/leftIcon").instance(2)')
            push_return_result_page_button.click()
            push_return_result_page_button.click()
        except Exception as e:
            print("ERROR: push_return_result_page_button not found", str(e))



    def find_filtre(self):
        #Swipe to find Sırala
        try:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(430, 1686)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(403, 916)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        except Exception as e:
            print("ERROR: Error occurred during swipe operation ->", str(e))

        try:

            self.push_filtre_button()
        except Exception as e:
            print("ERROR: push_filtre_button not found or clickable ->", str(e))


    def select_highest_price_sort(self):
        #Selecet 'En yüksek Fiyat'
        self.push_highest_price_button()

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(475, 1385)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(514, 665)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(455, 1798)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()







