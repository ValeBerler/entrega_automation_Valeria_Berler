from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        
        LoginPage(driver).login_completo(usuario,password)

        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        inventory_page.agregar_primer_producto()

        # Abrir el carrito
        inventory_page.abrir_carrito()

        # Validar el producto
        cartPage = CartPage(driver)
        
        productos_en_carrito = cartPage.obtener_productos_carrito()
        assert len(productos_en_carrito) == 1, "El carrito debe contener un producto."
        #assert False, "Fallo de prueba forzado"

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise