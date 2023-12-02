import sys
from gestores.GestorModel import GestorModel
from actividades.ActividadModel import ActividadModel

class GestorView:
    
    def __init__(self):
        self.gestor = GestorModel()
        self.actividad=ActividadModel()
        self.choices = { 
            "1": self.mostrarEstadoForma,
            "2": self.mostrarDeportistasMasActivos,
            "3": self.quit
        }
        
    def displayMenu(self):
        print(""" Opciones: \n
              1.- Mostrar el estado de forma \n
              2.- Obtener deportistas más activos por tipo de actividad
              3.- Salir 
              """)
        
    def run(self):
        while True:
            self.displayMenu()
            choice = input("Introducir opción: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} no es una opción válida".format(choice))
                
    def mostrarEstadoForma(self):
        correos=self.actividad.correovalido()
        while True:
            correo_electronico = input("Correo electrónico del atleta:")
            if correo_electronico in correos:
                break
            else:
                print("No existe usuario con este email")
        estado_de_forma = self.gestor.calcularEstadoForma(correo_electronico)
        if estado_de_forma < 1:
            print("Estado de forma malo")
        elif estado_de_forma == 1:
            print("Buena forma")
        else:
            print("Muy buena forma")

    def mostrarDeportistasMasActivos(self):
        tipo_actividad = input("Introduce el tipo de actividad: ")
        atletas_activos = self.gestor.obtenerDeportistasMasActivos(tipo_actividad)
        if atletas_activos:
            print("Atletas más activos en el tipo de actividad '{}':".format(tipo_actividad))
            for atleta in atletas_activos:
                print("Nombre de usuario: {}, Fecha de Alta: {}, Total de Actividades: {}".format(atleta['nombre_atleta'], atleta['fecha_alta'], atleta['total_actividades']))
        else:
            print("No se encontraron atletas activos para el tipo de actividad '{}'".format(tipo_actividad))

    def quit(self):
        print("Cerrando opciones.")
        sys.exit(0)