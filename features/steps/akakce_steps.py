from behave import given, when, then
from pages.login_page import LoginPage
from pages.notification_skip import NotificationSkip
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.result_page import ResultPage
from pages.search_result_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage

@given('Kullanıcı Akakçe uygulamasını açar')
def step_impl(context):
    # We cannot perform any additional action because the application is already open.
    pass

@when('Üye olmadan devam et seçeneğine tıklar')
def step_impl(context):
    login_page = LoginPage()
    notification_skip = NotificationSkip()
    notification_skip.notification_dont_allow()
    login_page.skip_login()

@when('Arama kutusuna "Laptop" yazar ve arar')
def step_impl(context, ):
    home_page = HomePage()
    home_page.click_serach_button()
    search_page=SearchPage()
    search_page.search_product("Laptop")

@when('Filtrele butonuna tıklar')
def step_impl(context):
    search_results_page = SearchResultsPage()
    search_results_page.click_filter_button()

@when('Alt Kategori olarak "Bilgisayar, Donanım" seçer ve Ürünleri Gör butonuna tıklar')
def step_impl(context, category):
    result_page = ResultPage()
    result_page.click_show_products_button()

@when('Sıralama seçeneklerinden "En yüksek Fiyat" seçer')
def step_impl(context, sort_option):
    result_page = ResultPage()
    result_page.find_filtre()
    result_page.select_highest_price_sort()


@when('Sonuç ekranından 10. ürüne tıklar')
def step_impl(context):
    search_results_page = SearchResultsPage()
    search_results_page.find_and_click_10th_highest_price()

@when('Ürüne Git butonuna tıklar')
def step_impl(context):
    product_detail_page = ProductDetailPage()
    product_detail_page.click_go_to_product_button()

@then('Ürün detay ekranında "{button_text}" butonunun görüntülendiğini doğrular')
def step_impl(context, button_text):
    product_detail_page = ProductDetailPage()
