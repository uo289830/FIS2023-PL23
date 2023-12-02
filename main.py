from atletas.AtletaView import AtletaView
from actividades.ActividadView import ActividadView
from gestores.GestorView import GestorView
from entidades.EntidadView import EntidadView
from util.database import DataBase
from dateutil.relativedelta import relativedelta

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. AtletaView")
    print("2. ActividadView")
    print("3. GestorView")
    print("4. EntidadView")
    print("5. Salir")
    

def programa_principal():
    DBNAME = "deporte.db"
    SCHEMA = "resources/schema.sql"
    DATA = "resources/data.sql"

    db = DataBase(DBNAME)  # Conexión a la base de datos DBNAME, si no existe la crea
    db.executeScript(SCHEMA)  # Genera el esquema ejecutando el script SCHEMA
    db.executeScript(DATA)  # Carga inicial de datos especificada en el script DATA

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            AtletaView().run()
        elif opcion == "2":
            ActividadView().run()
        elif opcion == "3":
            GestorView().run()
        elif opcion=="4":
            EntidadView().run()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    programa_principal()
