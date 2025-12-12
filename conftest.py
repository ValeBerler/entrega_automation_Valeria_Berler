import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib
from datetime import datetime
import time
# uso target para guardar las capturas de pantalla 
target = pathlib.Path("reports/screens")
# crear la carpeta reports/screens si no existe
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox") # las siguientes 4 líneas son para github actions
    options.add_argument("--disable-gpu") # para ahorrar recursos
    options.add_argument("--window-size=1920,1080") # para que tome toda la pantalla
    options.add_argument("--headless=new") # para que no abra la ventana del navegador


    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield

    report = outcome.get_result()

    if report.when in ("setup","call") and report.failed:
        driver = item.funcargs.get("driver",None)
        
        if driver:
            timestamp_comun= datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamp_unix = int(time.time())
            # Guardar la captura de pantalla con el formato especificado
            # report.when es el momento donde fallo
            # item.name es el nombre del test que falló
            file_name= target / f"{report.when}_{item.name}_{timestamp_comun}.png"
            # Guardar la captura de pantalla con el nombre que le especifiqué
            driver.save_screenshot(str(file_name))