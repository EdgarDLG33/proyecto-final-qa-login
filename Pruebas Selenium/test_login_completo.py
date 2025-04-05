
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def print_result(success, message):
    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")

try:
    driver.get("http://127.0.0.1:5000/login")
    time.sleep(1)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(2)
    print_result("Bienvenido" in driver.page_source, "Login exitoso")

    driver.find_element(By.LINK_TEXT, "Cerrar sesión").click()
    time.sleep(1)
    print_result("Iniciar sesión" in driver.page_source, "Cierre de sesión exitoso")

    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("mala123")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(1)
    print_result("Credenciales inválidas" in driver.page_source, "Mensaje por contraseña incorrecta")

    driver.get("http://127.0.0.1:5000/login")
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(1)
    print_result("Iniciar sesión" in driver.page_source, "Manejo de campos vacíos (sin error visible, solo recarga)")

    driver.get("http://127.0.0.1:5000/dashboard")
    time.sleep(1)
    print_result("Iniciar sesión" in driver.page_source, "Bloqueo de acceso directo a dashboard sin sesión")

except Exception as e:
    print("❌ Error durante la ejecución de pruebas:", e)

finally:
    driver.quit()
