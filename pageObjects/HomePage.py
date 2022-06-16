from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def signup_link(self):
        return self.driver.find_element(By.ID, "signin2")
# driver.find_element(By.ID, "signin2").click()  # Click on signup link