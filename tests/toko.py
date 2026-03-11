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

def clear_input(driver, by, locator):
    element = driver.find_element(by, locator)
    driver.execute_script("""
        arguments[0].value = '';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    """, element)
    return element

try:
    # --- AbNormal case ---
    wait = WebDriverWait(driver, 10)
    name_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    password_random = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    nomor_random = ''.join(random.choices(string.digits, k=11))
    nomor = "08" + nomor_random
    gmail = name_random + "@gmail.com"

    # tes case 1
    driver.get("https://auth-posajaumkm.posfin.id/login")
    time.sleep(5)

   

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("agungprakasa49@gmail.com")
    password_input.send_keys("AAaa123$")

    # --- Klik tombol login ---
    daftar_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Masuk']]"))
    )
    daftar_button.click()

    time.sleep(5)

    print("Berhasil Login")

    # Buat Toko

    klik_profile = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'ant-avatar ant-avatar-circle ant-avatar-image !w-10 !h-10 css-mbtvbp')]"))
    )
    klik_profile.click()

    driver.get("https://seller-posajaumkm.posfin.id/dashboard/profile")
    time.sleep(2)
    info_toko = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Info Toko']]"))
    )
    info_toko.click()
    time.sleep(2)


    file_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file' and @accept='image/*']"))
    )
    # Kirimkan path file lokal ke input file
    # file_path = r"D:/Tools/selenium/Posaja_UMKM_Posfin/tests/foto.png" 
    file_path = r"tests/foto.png" 
     # Gunakan path absolut
    file_input.send_keys(file_path)
    time.sleep(5)

    print("File berhasil diupload (dikirim ke input).")
    time.sleep(3)  # Tunggu sebelum quit (opsional)

    name_input = clear_input(driver, By.ID, "name")
    name_input.clear()
    time.sleep(2)
    name_input.send_keys(Keys.CONTROL + 'a')
    name_input.send_keys(Keys.BACKSPACE)
# Lalu kirim teks baru
    name_input.send_keys("Agung Posaja")
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.send_keys("088218320463")
    # alamat_input = driver.find_element(By.ID, "rc_select_0")
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-selector')]")))
    dropdown.click()
    alamat_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'ant-select-selection-search-input')]"))
    )
    alamat_input.send_keys("bandung")
    time.sleep(3)
    option = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@class, 'ant-select-item-option') and .//div[text()='Bandung, Bandung Raya, Indonesia']]"
        ))
    )
    driver.execute_script("arguments[0].click();", option)
    time.sleep(10)
    
    button_isialamat = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Lanjut Isi Alamat']]"))
    )
    button_isialamat.click()
    detail_alamat_input = clear_input(driver, By.ID, "address.address")
    tiktok_input = clear_input(driver,By.ID, "social_media[0].username")
    ig_input = clear_input(driver,By.ID, "social_media[1].username")
    fb_input = clear_input(driver,By.ID, "social_media[2].username")
    detail_alamat_input.clear()
    time.sleep(2)
    detail_alamat_input.send_keys(Keys.CONTROL + 'a')
    detail_alamat_input.send_keys(Keys.BACKSPACE)
    detail_alamat_input.send_keys("Jl gagak gang reuma kidul 2")
    tiktok_input.clear()
    tiktok_input.send_keys(Keys.CONTROL + 'a')
    tiktok_input.send_keys(Keys.BACKSPACE)
    tiktok_input.send_keys("agungprakasa")
    ig_input.clear()
    ig_input.send_keys(Keys.CONTROL + 'a')
    ig_input.send_keys(Keys.BACKSPACE)
    ig_input.send_keys("agungprakasa")
    fb_input.clear()
    fb_input.send_keys(Keys.CONTROL + 'a')
    fb_input.send_keys(Keys.BACKSPACE)
    fb_input.send_keys("agungprakasa")
    button_simpan = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Simpan']]"))
    )
    driver.execute_script("arguments[0].click();", button_simpan)
    driver.save_screenshot("output/berhasilupdatetoko.png")
    time.sleep(10)
    
finally:
    driver.quit()
