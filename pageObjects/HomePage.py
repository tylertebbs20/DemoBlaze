import time
import calendar
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    username = "auto_user" + str(time_stamp)  # Create unique user with timestamp
    password = "P@$$w0rd"

    def select_signup_link(self):
        return self.driver.find_element(By.ID, "signin2").click()  # Click on Sign In link

    def enter_username_on_signup(self):
        return self.driver.find_element(By.ID, "sign-username").send_keys(HomePage.username)  # Enter username on Signup modal

    def enter_password_on_signup(self):
        return self.driver.find_element(By.ID, "sign-password").send_keys(HomePage.password)  # Enter password on Signup modal

    def select_signup_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()  # Click on Sign Up button

    def select_login_link(self):
        return self.driver.find_element(By.ID, "login2").click()  # Click on login link

    def enter_username_on_login(self):
        return self.driver.find_element(By.ID, "loginusername").send_keys(HomePage.username)  # Enter username on Login modal

    def enter_password_on_login(self):
        return self.driver.find_element(By.ID, "loginpassword").send_keys(HomePage.password)  # Enter password on Login modal

    def select_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()  # Click login button

    def product_page_by_name(self, name):
        return self.driver.find_element(By.LINK_TEXT, name).click()  # Go to product page by name

    def select_product_store_logo(self):
        return self.driver.find_element(By.ID, "nava").click()  # Navigate back to home page

    def select_cart_link(self):
        return self.driver.find_element(By.ID, "cartur").click()  # Navigate to cart page

    def select_logout_link(self):
        return self.driver.find_element(By.ID, "logout2").click()  # Click on logout link

    def select_homepage_link(self):
        return self.driver.find_element(By.ID, "nava").click()  # Navigate back to home page

