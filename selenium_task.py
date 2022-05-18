from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

HOMEPAGE_CONTAINER_ELEMENT = '//div[contains(@class,"homepage-container")]'
CATEGORY_CONTAINER_ELEMENT = '//div[@class="product-list-container"]'
PRODUCT_DETAIL_ELEMENT = '//div[@class="product-detail"]'
ACCESSORIES_CATEGORY_LINK = "//a[@class='menu-header-item__title'][normalize-space()='Aksesuar']"
ALL_ACCESSORIES_CATEGORY_LINK = "//li//a[normalize-space()='Tüm Aksesuar Ürünleri']"
CART_CONTAINER_ELEMENT = "//div[contains(@class,'cart-container')]"
FIRST_PRODUCT = "//div[@class='product-image'][1]"
ADD_TO_CART_BUTTON = "//div//a[@id='pd_add_to_cart']"
CART_PRODUCT = "//a[@optionid='%s']"
CART_PAGE = "shopping-cart"
FAVORITE_BUTTON = "//a[@title='Favoriye Ekle']"
MAIN_PAGE = '//a[@class="main-header-logo"]'


def test_selenium_case():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.lcwaikiki.com/tr-TR/TR")
    time.sleep(1)
    assert driver.find_element(By.XPATH, HOMEPAGE_CONTAINER_ELEMENT)

    accessories_category = driver.find_element(By.XPATH, ACCESSORIES_CATEGORY_LINK)
    ActionChains(driver).move_to_element(accessories_category).perform()
    driver.find_element(By.XPATH, ALL_ACCESSORIES_CATEGORY_LINK).click()
    assert driver.find_element(By.XPATH, CATEGORY_CONTAINER_ELEMENT)
    time.sleep(1)
    driver.find_element(By.XPATH, FIRST_PRODUCT).click()

    time.sleep(1)
    assert driver.find_element(By.XPATH, PRODUCT_DETAIL_ELEMENT)
    product_id = driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).get_attribute('optionid')
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.ID, CART_PAGE).click()
    time.sleep(1)

    assert driver.find_element(By.XPATH, CART_CONTAINER_ELEMENT)
    cart_product_id = driver.find_element(By.XPATH, FAVORITE_BUTTON)
    assert product_id, cart_product_id

    driver.find_element(By.XPATH, MAIN_PAGE).click()
    assert driver.find_element(By.XPATH, HOMEPAGE_CONTAINER_ELEMENT)

    driver.close()


test_selenium_case()
