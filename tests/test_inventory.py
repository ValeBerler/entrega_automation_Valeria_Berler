from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        inventory_page = InventoryPage(driver)

        # Verificar que hay productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario esta vacio"

        # Verificar vacio el carrito al inicio
        assert inventory_page.obtener_conteo_carrito() == 0

        # Agregar el primer producto
        inventory_page.agregar_primer_producto()

        # Verificar el contador del carrito
        assert inventory_page.obtener_conteo_carrito() == 1
       
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise

