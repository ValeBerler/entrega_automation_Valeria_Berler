# Proyecto de Talento Tech

## Proposito del proyecto
Este proyecto tiene como objetivo automatizar pruebas de UI y de API para el sitio **SauceDemo**, aplicando practicas como Page Object Model, manejo de datos externos, generacion de reportes HTML, logging y captura automatica de pantalla.

## Tecnologias utilizadas
- Python 3.x
- Pytest
- Selenium WebDriver
- Logging
- Faker
- CSV / JSON
- Request

## Reportes y Logs

El proyecto genera tres tipos principales de resultados durante la ejecucion de las prubas: **reporte HTML**, **capturas de pantalla**, **archivo de log**

### Reporte HTML
Se genera un reporte HTML detallado con el nombre de ```reporte.hmtl``` en la **carpeta raiz** del proyecto

### Logs de ejecución
Tambien se genera un log con informacion detallada de toda la ejecución de las pruebas en la siguiente ubicacion: ```logs/suite.log```

### Capturas de pantalla

Se realizan capturas de pantalla por cada test que haya fallado y se encuentran en la siguiente ubicacion: ```reports/screens/```

## Ejuctar todas las pruebas
Para iniciar la ejecucion de las pruebas debes ejecutar la siguiente linea:

```bash
python -m run_test.py
```

## ¿Como interpretar los reportes?
- Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz.
- El reporte incluye:
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas

## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la pagina de inventario
- Comportamiento de la pagina del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP, validaciones de estructura JSON

## Manejo de datos de prueba
- En la carpeta `datos` se incluyen archivos como:
    - `data_login.csv` -> datos de usuarios validos o invalidos
    - `productos.json` -> datos de productos para validacion

### Conclusion
Este proyecto ofrece una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. Incluye un flujo simple de ejeucion mediante `run_test.py`, generacion automatica de reporte HTML facilitando el analisis de las pruebas.

La arquitectura del proyecto esta pensada para agregar nuevos casos de prueba y configuraciones sin modificar el nucleo del proyecto, manteniendo buenas practicas y permitiendo su escalabilidad en el tiempo.