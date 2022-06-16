from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def wait_til_alert_present(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()  # Close alert

