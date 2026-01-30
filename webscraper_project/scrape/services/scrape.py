from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import os
from datetime import datetime

def scrape_website():
    screenshots_dir = "/app/screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    # Configurar Selenium
    options = Options()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--no-sandbox')  # Requerido para algunos servidores
    options.add_argument('--disable-dev-shm-usage')  # Para evitar errores de memoria

    # Configurar el servicio de GeckoDriver
    service = Service("/usr/local/bin/geckodriver")
    # Crear el WebDriver de Firefox
    driver = webdriver.Firefox(service=service, options=options)

    # Navegar al sitio web
    url = "https://quotes.toscrape.com/"
    driver.get(url)
    print(f"URL confirmada: {driver.current_url}")
# Esperar a que los elementos estén presentes
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1"))
        )  # <--- Fíjate que aquí se cierra el paréntesis del wait

        # AHORA SÍ: Tomar captura de pantalla (fuera del wait)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"captura_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en: {screenshot_path}")

        authors = driver.find_elements(By.CSS_SELECTOR, ".author")
        quotes = driver.find_elements(By.CSS_SELECTOR, ".text")
    except Exception as e:
        print("Error al encontrar los elementos:", e)
        driver.quit()
        return []

    scraped_data = []
    for author, quote in zip(authors, quotes):
        scraped_data.append({
            "author": author.text,
            "quote": quote.text,
        })

    print("Scraped data:", scraped_data)  # Para depuración
    driver.quit()
    return scraped_data