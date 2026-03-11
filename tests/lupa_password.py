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
    wait = WebDriverWait(driver, 10)
    name_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    password_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    nomor_random = ''.join(random.choices(string.digits, k=11))
    nomor = "08" + nomor_random
    gmail = name_random + "@gmail.com"
    # ---test case 1
    driver.get("https://auth-posajaumkm.posfin.id/forgot-password")
    time.sleep(5)

   

    username_input = driver.find_element(By.ID, "username")

    username_input.send_keys(gmail)

    daftar_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Kirim']]"))
    )
    daftar_button.click()
    driver.save_screenshot("output/lupapasswordfailemail.png")
    time.sleep(5)

    print("Uji AbNormal - menggunakan email yang tidak terdaftar .")

    # ---test case 2
    driver.get("https://auth-posajaumkm.posfin.id/forgot-password")
    time.sleep(5)

   

    username_input = driver.find_element(By.ID, "username")

    username_input.send_keys(nomor)

    daftar_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Kirim']]"))
    )
    daftar_button.click()
    
    time.sleep(5)
    driver.save_screenshot("output/lupapasswordfailnomor.png")
    print("Uji AbNormal - menggunakan nomor yang tidak terdaftar .")
    # ---test case 3
    driver.get("https://auth-posajaumkm.posfin.id/forgot-password")
    time.sleep(5)

   

    username_input = driver.find_element(By.ID, "username")

    username_input.send_keys("agungprakasa49@gmail.com")

    daftar_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Kirim']]"))
    )
    daftar_button.click()
    time.sleep(5)
    driver.save_screenshot("output/lupapasswordberhasil.png")
    print("Uji Normal - menggunakan email yang terdaftar .")


finally:
    driver.quit()