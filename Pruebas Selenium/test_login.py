
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("http://127.0.0.1:5000/login")
    driver.maximize_window()
    time.sleep(1)

    assert "Iniciar sesión" in driver.page_source

    usuario_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    usuario_input.send_keys("admin")
    password_input.send_keys("admin123")
    password_input.send_keys(Keys.RETURN)

    time.sleep(2)
    assert "Bienvenido" in driver.page_source
    print("✅ Login exitoso")

    logout_button = driver.find_element(By.LINK_TEXT, "Cerrar sesión")
    logout_button.click()

    time.sleep(2)
    assert "Iniciar sesión" in driver.page_source
    print("✅ Cierre de sesión exitoso")

except AssertionError as e:
    print("❌ Falló alguna validación:", e)

finally:
    driver.quit()
