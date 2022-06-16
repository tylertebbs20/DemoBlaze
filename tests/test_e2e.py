import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from pageObjects.CartPage import CartPage
from utilities.BaseClass import BaseClass


s = Service("C:\\geckodriver.exe")
driver = webdriver.Firefox(service=s)
driver.implicitly_wait(10)  # seconds
driver.get("https://www.demoblaze.com/")


homepage = HomePage(driver)  # Initialize homepage object
product_page = ProductPage(driver)   # Initialize product_page object
cart_page = CartPage(driver)  # Initialize cart_page object


homepage.select_signup_link()  # Click on signup link
homepage.enter_username_on_signup()  # Enter username on Signup modal
homepage.enter_password_on_signup()  # Enter password on Signup modal
homepage.select_signup_button()   # Click on Sign Up button

wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert

homepage.select_login_link()  # Click on login link
homepage.enter_username_on_login()   # Enter username on Login modal
homepage.enter_password_on_login()  # Enter password on Login modal
homepage.select_login_button()  # Click login button

wait = WebDriverWait(driver, 10)
wait.until(EC.invisibility_of_element_located((By.ID, "logInModal")))

homepage.product_page_by_name("Samsung galaxy s6")  # Go to Samsung Galaxy s6 page
product_page.add_to_cart("a[onclick='addToCart(1)']")  # Click add to cart


wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert

homepage.select_product_store_logo()  # Navigate back to home page
homepage.product_page_by_name("Nokia lumia 1520")  # Go to Nokia Lumia 1520 page
product_page.add_to_cart("a[onclick='addToCart(2)']")  # Click add to cart


wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert

homepage.select_cart_link()  # Navigate to cart page
cart_page.select_place_order_button()  # Click on the Place Order button
cart_page.enter_place_order_name("Tyler Tebbs")  # Enter name in Name field
cart_page.enter_place_order_country("United States of America")  # Enter country in Country field
cart_page.enter_place_order_city("Orem")  # Enter city in City field
cart_page.enter_place_order_card("1111 2222 3333 4444")  # Enter credit card num in Credit Card field
cart_page.enter_place_order_card_month("05")  # Enter expiration month in Month field
cart_page.enter_place_order_card_year("2023")  # Enter year in Year field


wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='purchaseOrder()']/parent::div/button[1]")))
time.sleep(1)

cart_page.select_close_button()  # Click close button

all_delete_links = cart_page.all_delete_links()  # Find all Delete Links
for i in range(0, len(all_delete_links)):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal-backdrop fade']")))
    cart_page.click_delete_link()  # Delete Item in cart

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, "logout2")))

homepage.select_logout_link()  # Click on logout link
homepage.select_login_link()  # Click on login link
homepage.enter_username_on_login()  # Enter username on Login modal
homepage.enter_password_on_login()  # Enter password on Login modal
homepage.select_login_button()  # Click login button

wait = WebDriverWait(driver, 10)
wait.until(EC.invisibility_of_element_located((By.ID, "logInModal")))

homepage.select_cart_link()  # Navigate to cart page

products_in_cart = cart_page.all_products_in_cart()
assert not len(products_in_cart)  # assert there are no rows (products) in cart

homepage.select_homepage_link()   # Navigate back to home page
homepage.product_page_by_name("Nexus 6")  # Go to Nexus 6 page
product_page.add_to_cart("a[onclick='addToCart(3)']")  # Click add to cart button

wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert

homepage.select_cart_link()  # Navigate to cart page
