import csv
import json
import pathlib

RUTA_DATOS = pathlib.Path(__file__).parent.parent / "datos"


def leer_csv_login(ruta_archivo=None):
    """
    Lee el archivo CSV de credenciales de login.
    Retorna lista de tuplas (usuario, clave, debe_funcionar, descripcion)
    para usar en pytest.mark.parametrize.
    """
    datos = []
    ruta = pathlib.Path(ruta_archivo) if ruta_archivo else RUTA_DATOS / "login.csv"

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertir string 'True'/'False' a booleano
            debe_funcionar = fila["debe_funcionar"].lower() == "true"
            datos.append(
                (fila["usuario"], fila["clave"], debe_funcionar, fila["descripcion"])
            )

    return datos


def leer_json_productos(ruta_archivo=None):
    """
    Lee el archivo JSON de productos.
    Retorna lista de productos (dicts con nombre, precio y descripcion)
    para usar en pytest.mark.parametrize.
    """
    ruta = pathlib.Path(ruta_archivo) if ruta_archivo else RUTA_DATOS / "productos.json"

    with open(ruta, "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    return productos
