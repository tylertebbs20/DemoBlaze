from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def select_place_order_button(self):
        return self.driver.find_element(By.XPATH, "//button[@data-target='#orderModal']").click()  # Click On Place Order button

    def enter_place_order_name(self, name):
        return self.driver.find_element(By.ID, "name").send_keys(name)  # Enter name in Name field

    def enter_place_order_country(self, country):
        return self.driver.find_element(By.ID, "country").send_keys(country)  # Enter country in Country field

    def enter_place_order_city(self, city):
        return self.driver.find_element(By.ID, "city").send_keys(city)  # Enter city in City field

    def enter_place_order_card(self, card_num):
        return self.driver.find_element(By.ID, "card").send_keys(card_num)  # Enter credit card num in Credit Card field

    def enter_place_order_card_month(self, card_month):
        return self.driver.find_element(By.ID, "month").send_keys(card_month)  # Enter expiration month in Month field

    def enter_place_order_card_year(self, card_year):
        return self.driver.find_element(By.ID, "year").send_keys(card_year)  # Enter year in Year field

    def select_close_button(self):
        return self.driver.find_element(By.XPATH, "//button[@onclick='purchaseOrder()']/parent::div/button[1]").click()  # Click close

    def all_delete_links(self):
        return self.driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr/td[4]/a")

    def click_delete_link(self):
        return self.driver.find_element(By.XPATH, "//tbody[@id='tbodyid']/tr/td[4]/a").click()  # Delete item in cart.

    def all_products_in_cart(self):
        return self.driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")  # all products (rows) in cart

