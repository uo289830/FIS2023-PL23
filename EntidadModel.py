from util.database import DataBase
import sqlite3
from datetime import datetime, timedelta
from util.checkdate import DateChecker  # Asegúrate de importar la clase DateChecker

class EntidadModel:
    
    def __init__(self):
        self.db = DataBase("deporte.db")
        
      # Inserción de los datos de una actividad (historia de usuario1 - Adriana)
    def insertActividadEntidad(self,nombre_entidad, nombre_actividad, descripcion, fecha, duracion,hora_inicio, localizacion,plazas, coste,info_ad):
        while True:
            if not DateChecker.checkdateEntidad(fecha):
                print("La fecha no cumple con el formato esperado (aaaa-mm-dd).")
                fecha = input("Por favor, ingrese la fecha nuevamente (aaaa-mm-dd): ")
            else:
                break  # La fecha es válida, salimos del bucle
        query = """
                INSERT INTO ActividadEntidades(nombre_entidad, nombre_activ_entidad ,descripcion ,fecha ,duracion_dias,hora_inicio,lugar,plazas,coste_UsFree,info_adicional)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)
                """
        self.db.executeUpdateQuery(query,nombre_entidad, nombre_actividad, descripcion, fecha, duracion,hora_inicio, localizacion,plazas, coste,info_ad)
