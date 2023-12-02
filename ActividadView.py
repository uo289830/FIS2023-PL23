import sys
from actividades.ActividadModel import ActividadModel

class ActividadView:
    
    def __init__(self):
        self.actividad=ActividadModel()
        self.choices= { "1": self.nuevaActividad,
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

    def nuevaActividad(self):
        fecha = input("Fecha de la actividad (aaaa-mm-dd):")
        duracion = input("Duración de la actividad:")
        localizacion = input("Lugar en el que se realizó la actividad:")
        distancia = input("Distancia recorrida:")
        FCmax = input("FCmax:")
        FCmin = input("FCmin:")
        nombreActividad = input("Nombre de la categoria:")
        actividades=self.actividad.actividades_disp()
        print("Lista de actividades disponibles:")
        i=1
        listaact=[]
        for actividad in actividades:
            print(f"{i}-{actividad['nombre_subtipo']}")
            listaact.append(actividad['nombre_subtipo'])
            i+=1
        print(listaact)
        while True:
            nombreSubtipo=input("Nombre de la actividad:")
            if nombreSubtipo in listaact:
                break
            else:
                print("Nombre de actividad inválido")
        correos=self.actividad.correovalido()
        while True:
            correo_electronico = input("Correo electrónico del atleta:")
            if correo_electronico in correos:
                break
            else:
                print("No existe usuario con este email")
        
        self.actividad.insertActividad(nombreActividad,nombreSubtipo, fecha, duracion, localizacion, distancia, FCmax, FCmin, correo_electronico)
        
    
    def quit(self):
        print("Cerrando opciones.")
        sys.exit(0) 
        