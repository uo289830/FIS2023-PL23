from util.database import DataBase
import sqlite3
from datetime import datetime, timedelta
from util.checkdate import DateChecker


class ActividadModel:
    
    def __init__(self):
        self.db = DataBase("deporte.db")
        

    def actividades_disp(self):
        query = "SELECT nombre_subtipo FROM Subtipos;"
        actividades = self.db.executeQuery(query)
        return actividades
    
    def correovalido(self):
        query = "SELECT correo_electronico FROM Atletas;"
        correos = self.db.executeQuery(query)
        emails = []
        for correo in correos:
            emails.append(correo['correo_electronico'])
        return emails
    
    def insertActividad(self, nombre_actividad, nombre_subtipo, fecha, duracion, localizacion, distancia, FCmax, FCmin, correo_electronico):
        # Verifica si la fecha tiene el formato válido
        if not DateChecker.checkdate(fecha):
            print("Error: La fecha no tiene el formato válido (aaaa-mm-dd).")
            return
        
        # Verifica si el atleta es "Free" y ha alcanzado el límite de tipos/subtipos
        if self.esDeportistaFree(correo_electronico):
            tipos_actuales = self.obtenerTiposActividades(correo_electronico)
            if len(tipos_actuales) >= 3 and nombre_subtipo not in tipos_actuales:
                print("Error: Has alcanzado el límite de 3 tipos/subtipos diferentes para deportistas 'Free'.")
                return
        
        # Continúa con la inserción de la actividad
        query = """
            INSERT INTO Actividades(nombre_actividad, nombre_subtipo, fecha, duracion, localizacion, distancia, FCmax, FCmin, correo_electronico)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.executeUpdateQuery(query, nombre_actividad, nombre_subtipo, fecha, duracion, localizacion, distancia, FCmax, FCmin, correo_electronico)
        print("Actividad insertada")
        
    def esDeportistaFree(self, correo_electronico):
        query = "SELECT tipo_atleta FROM Atletas WHERE correo_electronico = ?"
        resultado = self.db.executeQuery(query, (correo_electronico,))
        
        # Verifica si el deportista es de tipo "Free"
        return resultado and resultado[0]['tipo_atleta'] == 'Free'

    def obtenerTiposActividades(self, correo_electronico):
        query = "SELECT DISTINCT(nombre_subtipo) FROM Actividades WHERE correo_electronico = ?"
        tipos_actividades = self.db.executeQuery(query, (correo_electronico,))
        
        # Convierte la lista de resultados a una lista de tipos
        return [tipo['nombre_subtipo'] for tipo in tipos_actividades]    