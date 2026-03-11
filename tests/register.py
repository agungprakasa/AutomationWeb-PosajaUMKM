from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random
import string



options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Remote(
    command_executor='http://10.24.7.14:4444/wd/hub',
    options=options
)
# driver = webdriver.Chrome()

try:
    # --- AbNormal case ---
    wait = WebDriverWait(driver, 15)
    name_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    gmail_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    gmail = gmail_random + "@gmail.com"
    
    driver.get("https://auth-posajaumkm.posfin.id/register")
    time.sleep(5)

   

    username_input = driver.find_element(By.ID, "full_name")
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "confirm_password")

    username_input.send_keys("Agung")
    email_input.send_keys("agungprakasa49@gmail.com")
    password_input.send_keys("AAaa123$")
    confirm_password_input.send_keys("AAaa123$")
    # click_setuju_button = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'ant-checkbox-input')]"))
    # )
    # click_setuju_button.click()

    checkbox = driver.find_element(By.CSS_SELECTOR, "input.ant-checkbox-input")
    if not checkbox.is_selected():
        checkbox.click()

    # --- Klik tombol login ---
    daftar_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Daftar']]"))
    )
    daftar_button.click()
    time.sleep(5)
    driver.save_screenshot("output/register_fail.png")

    print("Uji AbNormal - Email yang sudah terdaftar .")
    #  Normal Case Register
    driver.get("https://auth-posajaumkm.posfin.id/register")
    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    name_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    gmail_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    gmail = gmail_random + "@gmail.com"

    username_input = driver.find_element(By.ID, "full_name")
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "confirm_password")

    username_input.send_keys(name_random)
    email_input.send_keys(gmail)
    password_input.send_keys("AAaa123$")
    confirm_password_input.send_keys("AAaa123$")
    # click_setuju_button = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'ant-checkbox-input')]"))
    # )
    # click_setuju_button.click()

    checkbox = driver.find_element(By.CSS_SELECTOR, "input.ant-checkbox-input")
    if not checkbox.is_selected():
        checkbox.click()

    # --- Klik tombol login ---
    daftar_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Daftar']]"))
    )
    daftar_button.click()
    time.sleep(5)
    driver.save_screenshot("output/register_success.png")
    print("Uji Normal - Modul Register Berhasil .")


   
finally:
    driver.quit()
