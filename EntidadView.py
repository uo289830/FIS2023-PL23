import sys
from entidades.EntidadModel import EntidadModel

class EntidadView:
    
    def __init__(self):
        self.actividad_ent=EntidadModel()
        self.choices= { "1": self.nuevaActividadEntidad,
                         "2": self.quit
                       }
        
           
    def displayMenu (self):
        print(""" Opciones: \n
              1.- Introducir una nueva actividad \n
              2.- Salir 
              """)
        
    #Muestra la lista de opciones y permite la selección
    def run (self):
        while True:
            self.displayMenu()
            choice = input("Introducir opción: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} no es una opción valida".format(choice))
    
    
    #Vista para la HU1 Insertar una actividad (Adriana)
    def nuevaActividadEntidad(self):
        nombre_entidad=input("Nombre de la entidad:")
        nombreActividad = input("Nombre de la actividad:")
        descripcion=input("Breve descripcion de la a:")
        fecha = input("Fecha de la actividad (aaaa-mm-dd):")
        duracion = input("Duración de la actividad en días:")
        hora=input("Hora de inicio de la actividad:")
        localizacion = input("Lugar en el que se realizará la actividad:")
        plazas=input("Numero de plazas disponibles:")
        coste=input("Coste para usuarios FREE:")
        info=input("Información adicional acerca de la carrera o de gestion de inscripcion:")
       
        
        self.actividad_ent.insertActividadEntidad(nombre_entidad,nombreActividad,descripcion, fecha, duracion,hora, localizacion,plazas,coste,info)
        print("Actividad insertada")
    
    def quit(self):
        print("Cerrando opciones.")
        sys.exit(0) 
