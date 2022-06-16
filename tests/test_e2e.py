import time
import calendar
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from pageObjects.HomePage import HomePage



s = Service("C:\\geckodriver.exe")
driver = webdriver.Firefox(service=s)
driver.implicitly_wait(10)  # seconds
driver.get("https://www.demoblaze.com/")

current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)

# homepage = HomePage(self.driver)

username = "auto_user" + str(time_stamp)  # Unique user
password = "P@$$w0rd"

driver.find_element(By.ID, "signin2").click()  # Click on signup link
driver.find_element(By.ID, "sign-username").send_keys(username)  # Enter username on Signup modal
driver.find_element(By.ID, "sign-password").send_keys(password)  # Enter password on Signup modal
driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()  # Click on Sign Up button
wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert

driver.find_element(By.ID, "login2").click()  # Click on login link
driver.find_element(By.ID, "loginusername").send_keys(username)  # Enter username on Login modal
driver.find_element(By.ID, "loginpassword").send_keys(password)  # Enter password on Login modal
driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()  # Click login button

wait = WebDriverWait(driver, 10)
wait.until(EC.invisibility_of_element_located((By.ID, "logInModal")))

driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()  # Go to Samsung Galaxy s6 page
driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(1)']").click()  # Click add to cart button
wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert
driver.find_element(By.ID, "nava").click()  # Navigate back to product page
driver.find_element(By.LINK_TEXT, "Nokia lumia 1520").click()  # Go to Nokia Lumia 1520 page
driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(2)']").click()  # Click add to cart button
wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert
driver.find_element(By.ID, "cartur").click()  # Navigate to cart page
driver.find_element(By.XPATH,
                         "//button[@data-target='#orderModal']").click()  # Click On Place Order button
driver.find_element(By.ID, "name").send_keys("Tyler Tebbs")  # Enter name in Name field
driver.find_element(By.ID, "country").send_keys(
    "United States of America")  # Enter country in Country field
driver.find_element(By.ID, "city").send_keys("Orem")  # Enter city in City field
driver.find_element(By.ID, "card").send_keys(
    "1111 2222 3333 4444")  # Enter credit card number in Credit Card field
driver.find_element(By.ID, "month").send_keys("05")  # Enter expiration month in Month field
driver.find_element(By.ID, "year").send_keys("2023")  # Enter year in Year field

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='purchaseOrder()']/parent::div/button[1]")))
time.sleep(1)
driver.find_element(By.XPATH,
                         "//button[@onclick='purchaseOrder()']/parent::div/button[1]").click()  # Click close

all_delete_links = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr/td[4]/a")
for i in range(0, len(all_delete_links)):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal-backdrop fade']")))
    driver.find_element(By.XPATH,
                             "//tbody[@id='tbodyid']/tr/td[4]/a").click()  # Delete both items in cart.

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, "logout2")))
driver.find_element(By.ID, "logout2").click()  # Click on logout link

driver.find_element(By.ID, "login2").click()  # Click on login link
driver.find_element(By.ID, "loginusername").send_keys(username)  # Enter username on Login modal
driver.find_element(By.ID, "loginpassword").send_keys(password)  # Enter password on Login modal
driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()  # Click login button

wait = WebDriverWait(driver, 10)
wait.until(EC.invisibility_of_element_located((By.ID, "logInModal")))
driver.find_element(By.ID, "cartur").click()  # Navigate to cart page

table_rows = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")  # all rows in cart
assert not len(table_rows)  # assert there are no rows (products) in cart

driver.find_element(By.ID, "nava").click()  # Navigate back to product page
driver.find_element(By.LINK_TEXT, "Nexus 6").click()  # Go to Nexus 6 page
driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(3)']").click()  # Click add to cart button
wait = WebDriverWait(driver, 3)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()  # Close alert
driver.find_element(By.ID, "cartur").click()  # Navigate to cart page
