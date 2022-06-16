from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, element):
        return self.driver.find_element(By.CSS_SELECTOR, element).click()  # Click add to cart button