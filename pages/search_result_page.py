
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pages.base_page import BasePage




class SearchResultsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.filter_button = "com.akakce.akakce:id/filterButton"
        self.product_list = "com.akakce.akakce:id/productListRV"
        self.product_items = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.akakce.akakce:id/productListRV']"
        self.sort_button = "com.akakce.akakce:id/sortButton"
        self.sort_highest_price = "//android.widget.TextView[contains(@text, 'En Yüksek Fiyat')]"

    def click_filter_button(self):
        self.click(AppiumBy.ID, self.filter_button)

    def click_sort_button(self):
        self.click(AppiumBy.ID, self.sort_button)

    def select_highest_price_sort(self):
        self.click(AppiumBy.XPATH, self.sort_highest_price)

    # Add the missing functions
    def extract_price(self, price_text):
        """Extract numeric price value from text containing price"""
        match = re.search(r'([\d.,]+)', price_text)
        if match:
            # Convert price string to float value (replace comma with dot for decimal point)
            price_str = match.group(1).replace('.', '').replace(',', '.')
            return float(price_str)
        return 0

    def get_product_prices(self):
        """Find all price elements and extract their values"""
        # Looking for TextViews that contain price values with "TL"
        price_xpath = "//android.widget.TextView[@resource-id='com.akakce.akakce:id/price' "

        # Wait for prices to be visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, price_xpath))
        )

        # Find all elements containing price information
        price_elements = self.driver.find_elements(AppiumBy.XPATH, price_xpath)

        products = []
        for element in price_elements:
            try:
                price_text = element.text
                price_value = self.extract_price(price_text)
                product_info = {
                    "element": element,
                    "price_text": price_text,
                    "price_value": price_value
                }
                products.append(product_info)
                print(f"Found product with price: {price_text} -> {price_value}")
            except Exception as e:
                print(f"Error processing element: {e}")

        return products

    def find_product_by_index(self, index):
        """Find a product by its index (0-based)"""
        products = self.get_product_prices()

        # Sort products by price in descending order
        sorted_products = sorted(products, key=lambda x: x["price_value"], reverse=True)

        if 0 <= index < len(sorted_products):
            return sorted_products[index]
        else:
            raise IndexError(f"Product index {index} out of range. Only {len(sorted_products)} products found.")

    def click_nth_highest_priced_product(self, n):
        """Click on the nth highest priced product (n is 1-based, so 10 means 10th product)"""
        product = self.find_product_by_index(n - 1)  # Convert to 0-based index
        if product:
            product["element"].click()
            return True
        return False



    def find_and_click_10th_highest_price(self):
        try:
            # 1. Fiyat içeren tüm TextView'ları bul
            price_elements = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.TextView[@resource-id='com.akakce.akakce:id/price' "
            )

            # 2. İlk 13 fiyatı al
            price_elements = price_elements[:13]

            product_prices = []

            for price_element in price_elements:
                try:
                    price_text = price_element.text
                    price_number = int(price_text.replace(".", "").replace(",", "").replace("TL", "").strip())

                    product_prices.append((price_element, price_number))

                except Exception:
                    continue

            # 3. Fiyatlara göre azalan sıralama yap
            sorted_products = sorted(product_prices, key=lambda x: x[1], reverse=True)

            # 4. 10. ürünü bul ve tıkla
            if len(sorted_products) >= 10:
                tenth_price_element = sorted_products[9][0]
                print(f"10. yüksek fiyatlı ürünün fiyatı: {sorted_products[9][1]}")
                tenth_price_element.click()
            else:
                print("İlk 13 fiyatlı üründen 10'dan az fiyat bulundu.")

        except Exception as e:
            print("Hata oluştu:", str(e))

