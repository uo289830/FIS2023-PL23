import sys
from atletas.AtletaModel import AtletaModel
from datetime import datetime, timedelta
from gestores.GestorModel import GestorModel
from actividades.ActividadModel import ActividadModel
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import pandas as pd

class AtletaView:
    '''
    Clase que representa la vista (entrada y salida) de datos
    para las funcionalidades relativas a los atletas que estarán
    representadas en la clase AtletaModel (AtletaModel.py)
    '''
    def __init__ (self):
        self.atleta = AtletaModel () #Crea un objeto model que se invocará desde esta vista
        #Crea un diccionario con las opciones (key) y los métodos/acciones que se pueden realizar en este objeto (values)
        self.actividad=ActividadModel()
        self.choices = { "1": self.muestra_actividades,
                         "2":self.mostrar_resumen_atleta,
                         "3":self.showatletas,
                         "4":self.MuestraConsumoCalorico,
                         "5":self.generarInformeActividades,
                         "6":self.importarArchivoCsv,
                         "7":self.nuevaAtletaFree,
                         "8":self.nuevaAtletaPremium,
                         "9":self.introducir_Objetivos,
                         "10":self.seguimiento,
                         "11":self.inscripcion_actividad,
                         "12":self.cambiartipo,
                         "13":self.generar_graficos_atleta,
                         "14": self.quit
                       }
        
    def displayMenu (self):
        print(""" Opciones: \n
              1.- Listar actividades
              2.- Mostrar resumen actividad
              3.- Listar atletas de un tipo de actividad
              4.- Mostrar consumo calórico
              5.- Generar resumen mensual, anual, por tipo mensual y por tipo anual
              6.- Importar archivo csv
              7.- Registro de un usuario Free
              8.- Registro de un usuario Premium 
              9.- Introducir objetivos
              10.- Ver seguimiento
              11.- Inscripción a actividad externa
              12.- Cambiar de free a premium o viceversa
              13.- Generar gráficos
              14.- Salir 
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
    

    def quit(self):
        print("Cerrando opciones.")
        sys.exit(0)

    #Médodo muy general para imprimir los resultados (res) que vienen del model
    def printResults (self,res):
        if len(res)==0: 
            print ("No hay resultados")
        else:
            #cabecera
            print (list(res[0].keys())) # Imprime nombres de columnas (keys del diccionario)
            print ("----------------------------------")
            #contenido 
            for row in res:
                print ([*row.values()]) # Imprime valor de una fila (values del diccionario)
            print ("----------------------------------")
    

    def muestra_actividades(self):
        # Recupera y muestra los detalles de las actividades en el rango de fechas.
        correo_electronico=input("Correo electrónico:")
        fecha_inicio=input("Fecha de inicio de la actividad (aaaa-mm-dd):")
        fecha_fin=input("Fecha de fin de la actividad (aaaa-mm-dd):")
        actividades=self.atleta.busca_actividades(correo_electronico,fecha_inicio,fecha_fin)
        for actividad in actividades:
            print(f"ID de la actividad: {actividad['idactividad']}, Fecha: {actividad['fecha']}, Duración: {actividad['duracion']}, Distancia: {actividad['distancia']}, FCmax: {actividad['FCmax']}, FCmin: {actividad['FCmin']}, Nombre de la categoria: {actividad['nombre_actividad']}, Nombre de la actividad:{actividad['nombre_subtipo']}")
    
        


    def mostrar_resumen_atleta(self):
        correo_electronico = input("Correo electrónico: ")
        self.atleta.resumen(correo_electronico)
   
  
    def showatletas(self):
        nameactividad=input("Introduzca tipo de actividad:") 
        idactividad = self.atleta.getIdactividad(nameactividad)
        if idactividad==None:
            print ("No existe el tipo de actividad", nameactividad)
        correo_electronico=input("Introducir su correo electronico: ")
        correo_electronico2=input("Introducir el correo del atleta a comparar: ") 
        atletasPremium=self.atleta.getAtletasPremium()
        for atleta in atletasPremium:
            correo_actual = atleta['correo_electronico']
            if atleta['tipo_atleta'] == 'Premium':
                if correo_actual != correo_electronico and correo_actual != correo_electronico2:
                    res = self.atleta.historia2(nameactividad, correo_electronico2)
                    self.printResults(res)
                else:
                    print("No son dos usuarios Premium", correo_electronico, correo_electronico2)
            else:
                print(f"{correo_actual} no es un usuario Premium")
    """
    
    def showatletas (self):
        nameactividad = input ("Introducir tipo de actividad: ")
        correo_electronico2=input("Introducir su correo electronico: ")
        correo_electronico=input("Introducir el correo del atleta a comparar: ")    
        tipo_atleta2=self.atleta.getAtletasPremium(correo_electronico2)
        tipo_atleta=self.atleta.getAtletasPremium(correo_electronico)  
        idactividad = self.atleta.getIdactividad(nameactividad)
        if idactividad==None:
            print ("No existe el tipo de actividad", nameactividad)
        if tipo_atleta2=='Premium' and tipo_atleta=='Premium':
            res=self.atleta.historia2(nameactividad,correo_electronico)
            self.printResults(res)            
        else:
            print("El atleta no es premium")  
    """
    def MuestraConsumoCalorico(self):
        correos=self.actividad.correovalido()
        while True:
            correo_electronico = input("Correo electrónico del atleta:")
            if correo_electronico in correos:
                break
            else:
                print("No existe usuario con este email")
        fecha_inicio=input("Fecha de inicio de la actividad (aaaa-mm-dd):")
        fecha_fin=input("Fecha de fin de la actividad (aaaa-mm-dd):")
        peso=input("Peso en kg:")
        altura=input("altura en cm:")
        edad=input("Edad en años:")
        sexo=input("mujer/hombre:")
        self.atleta.calcularConsumo(correo_electronico,fecha_inicio,fecha_fin,peso,altura,edad,sexo)

    #h1s2 sara    
    

    def generarInformeActividades(self):
        correo_electronico = input("Correo electrónico: ")

        # Obtiene los resúmenes
        resumen_mensual = self.atleta.obtenerActividadesDelMes(correo_electronico)
        resumen_anual = self.atleta.obtenerActividadesDelAño(correo_electronico)
        resumen_tipo_actividad_mes = self.atleta.obtenerActividadesPorTipoDelMes(correo_electronico)
        resumen_tipo_actividad_año = self.atleta.obtenerActividadesPorTipoDelAño(correo_electronico)

        # Imprime los resúmenes
        print("\nResumen mensual:")
        self.printResumen(resumen_mensual)

        print("\nResumen anual:")
        self.printResumen(resumen_anual)

        print("\nResumen por tipo de actividad (mes):")
        self.printResumen(resumen_tipo_actividad_mes)

        print("\nResumen por tipo de actividad (año):")
        self.printResumen(resumen_tipo_actividad_año)

    def printResumen(self, resumen):
        # Verificar si resumen es una cadena (tabla PrettyTable)
        if isinstance(resumen, str):
            print(resumen)
        else:
            for clave, valor in resumen.items():
                print(f"{clave}: {valor}")

            
    #h2s2 sara    
    def importarArchivoCsv(self):
        correo_electronico = input("Correo electrónico: ")
        nombre_archivo = input("Ruta hasta el archivo: ")

        # Llamar a la función en el modelo
        self.atleta.importarActividadesDesdeCSV(nombre_archivo)        
        
     
    #Vista para la HU1 registrar un usuario Free
    def nuevaAtletaFree(self):
        Correo_electronico = input("Introduzca su corrreo electrónico:")
        Nombre = input("Introduzca su nombre:")
        Apellidos = input("Introduzca sus apellidos:")
        fecha_nacimiento = input("Fecha de nacimiento (aaa-mm-dd):")
        peso = input("Peso (en kg):")
        Altura = input("Altura (en cm):")
        tipo_atleta="Free"
        fecha_alta=datetime.now().date()
        Iban=None
        Numero_tarjeta=None
        fecha_caducidad=None
        Cvv=None        
        self.atleta.insertAtletaFree(Correo_electronico,Nombre,Apellidos,fecha_alta,fecha_nacimiento,peso,Altura,tipo_atleta,Iban,Numero_tarjeta, fecha_caducidad,Cvv)
    
    #Vista para la HU2 registrar un usuario Premium
    def nuevaAtletaPremium(self):
        Correo_electronico = input("Introduzca su corrreo electrónico:")
        Nombre = input("Introduzca su nombre:")
        Apellidos = input("Introduzca sus apellidos:")
        fecha_nacimiento = input("Fecha de nacimiento (aaa-mm-dd):")
        peso = input("Peso (en kg):")
        Altura = input("Altura (en cm):")
        tipo_atleta="Premium"
        fecha_alta=datetime.now().date()
        metodo_pago=input("Introduzca el método de pago (Transferencia/tarjeta):")
        if metodo_pago.upper()=="TRANSFERENCIA":
            Iban=input("Introduzca su IBAN de la cuenta:")
            Numero_tarjeta=None
            fecha_caducidad=None
            Cvv=None
        elif metodo_pago.upper()=="TARJETA":
            Numero_tarjeta=input("Introduzca su numero de tarjeta:")
            fecha_caducidad=input("Introduzca la fecha de caducidad de la tarjeta (mm-dd):")
            Cvv=input("Introduzca su CVV de la tarjeta:")
            Iban=None  
        else:
            print("El método de pago no es correcto")
            metodo_pago=input("Vuelva a introducir el método de pago (Transferencia/tarjeta):")
        self.atleta.insertAtletaPremium(Correo_electronico,Nombre,Apellidos,fecha_alta,fecha_nacimiento,peso,Altura,tipo_atleta,Iban,Numero_tarjeta, fecha_caducidad,Cvv)

    def introducir_Objetivos(self):
        correo_electronico=input("Introduzca su correo electrónico:")
        correo_electronico=correo_electronico.lower()
        while correo_electronico not in [correo['correo_electronico'].lower() for correo in self.atleta.getAtletas()]:
            print("EL correo no es válido")
            correo_electronico=input("Vuelva a introducir su correo electrónico:")
        tipo_objetivo=input("Introduzca el tipo de objetivo (Duracion/Actividades):")
        if tipo_objetivo.upper()=="DURACION":
            valor_objetivo=float(input("Introduzca el numero de horas objetivo:"))
        elif tipo_objetivo.upper()=="ACTIVIDADES":
            valor_objetivo=float(input("Introduzca el número de actividades objetivo:"))
        else:
            print("El tipo de objetivo no es válido")
            tipo_objetivo=input("Vuelva a introducir el tipo de objetivo (Duracion/Actividades):")
        self.atleta.objetivos(correo_electronico, tipo_objetivo, valor_objetivo)

    def seguimiento(self):
        correo_electronico=input("Introduzca su correo electrónico:")
        correo_electronico=correo_electronico.lower()
        while correo_electronico not in [correo['correo_electronico'].lower() for correo in self.atleta.getAtletas()]:
            print("EL correo no es válido")
            correo_electronico=input("Vuelva a introducir su correo electrónico:")
        fecha_inicio=input("Fecha de inicio de la actividad (aaaa-mm-dd):")
        fecha_fin=input("Fecha de fin de la actividad (aaaa-mm-dd):")
        num_horas = self.atleta.getnumhoras((correo_electronico, fecha_inicio, fecha_fin))
        num_actividades = self.atleta.getnumactividades((fecha_inicio, fecha_fin, correo_electronico))
        print(f"Número de actividades obtenido: {num_actividades}")
        Objetivos = self.atleta.getObjetivos(correo_electronico)
        gestor=GestorModel()
        estado_forma = gestor.calcularEstadoForma(correoElectronico=correo_electronico)
        for objetivo in Objetivos:
            if objetivo["tipo_objetivo"].upper()=="DURACION":
                if num_horas is not None and objetivo["valor_objetivo"]>=num_horas:
                    print(f"El numero de horas realizadas fueron {num_horas} horas y el objetivo {objetivo['valor_objetivo']} horas. Por tanto, se ha cumplido el objetivo con estado de forma: {estado_forma}")
                else:
                    print(f"El numero de horas realizadas fueron {num_horas} horas y el objetivo {objetivo['valor_objetivo']} horas. Por tanto, no se ha cumplido el objetivo con estado de forma: {estado_forma}")      

            elif objetivo["tipo_objetivo"].upper()=="ACTIVIDADES":
                if num_horas is not None and objetivo['valor_objetivo']>=num_actividades:
                    print(f"El numero de actividades realizadas fueron {num_actividades} actividades y el objetivo {objetivo['valor_objetivo']} horas. Por tanto, se ha cumplido el objetivo con estado de forma: {estado_forma}")
                else:
                    print(f"El numero de actividades realizadas fueron {num_actividades} actividades y el objetivo {objetivo['valor_objetivo']} horas. Por tanto, no se ha cumplido el objetivo con estado de forma: {estado_forma}")
        return 
        
        
    def inscripcion_actividad(self):
        correos=self.actividad.correovalido()
        while True:
            correo_electronico = input("Correo electrónico del atleta:")
            if correo_electronico in correos:
                break
            else:
                print("No existe usuario con este email")
        actividades=self.atleta.obtenerActividadesExternas()
        i=0
        for actividad in actividades:
            print(f"{i}. Nombre de la entidad: {actividad['nombre_entidad']}, Nombre de la actividad: {actividad['nombre_activ_entidad']}, Descripción: {actividad['descripcion']} Fecha: {actividad['fecha']}, Duración: {actividad['duracion_dias']}, Ubicación: {actividad['lugar']},Numero de plazas: {actividad['plazas']},Coste para ususarios FREE: {actividad['coste_UsFree']}")
            i+=1
        actividad_inscricion=input("Introduce el numero de actividad al que desea inscribirse:")
        actividad=actividades[int(actividad_inscricion)]
        self.atleta.registrar_inscripcion(correo_electronico,actividad)
       
        
        
    def cambiartipo(self):
        correos=self.actividad.correovalido()
        while True:
            correo_electronico = input("Correo electrónico del atleta:")
            if correo_electronico in correos:
                break
            else:
                print("No existe usuario con este email")    
        self.atleta.cambiarTipoAtleta(correo_electronico)
        
    def generar_graficos_atleta(self):
        correo_electronico=input("ingrese el correo electrónico")
        # Obtener datos del modelo
        subtipos = self.atleta.obtenerTiposActividades(correo_electronico)
        hoy=str(datetime.now())
        actividades = self.atleta.busca_actividades(correo_electronico, '2023-01-01', hoy)

        # Crear DataFrame de Pandas para facilitar la manipulación de datos
        df = pd.DataFrame(actividades)

        # Gráfico de Barras para Duración Total de cada Subtipo
        plt.figure(figsize=(10, 6))
        for subtipo in subtipos:
            duracion_total = df[df['nombre_subtipo'] == subtipo]['duracion'].sum()
            plt.bar(subtipo, duracion_total, label=subtipo)

        plt.xlabel('Subtipos de Actividades')
        plt.ylabel('Duración Total (minutos)')
        plt.title('Duración Total de Actividades por Subtipo')
        plt.legend()
        plt.show()

        # Gráfico de Líneas para la Progresión Temporal de la Duración Total
        df['fecha'] = pd.to_datetime(df['fecha'])
        df.sort_values(by='fecha', inplace=True)

        plt.figure(figsize=(12, 6))
        plt.plot(df['fecha'], df.groupby('fecha')['duracion'].sum().cumsum(), marker='o')
        plt.xlabel('Fecha')
        plt.ylabel('Duración Total Acumulada (minutos)')
        plt.title('Progresión Temporal de la Duración Total de Actividades')
        plt.show()

        # Gráfico Circular para la Distribución de Tipos de Actividad
        plt.figure(figsize=(8, 8))
        actividad_distribucion = df.groupby('nombre_subtipo')['duracion'].sum()
        plt.pie(actividad_distribucion, labels=actividad_distribucion.index, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title('Distribución de Tipos de Actividad por Duración Total')
        plt.show()

        # Histograma de la Distribución de Frecuencia de la Duración de la Actividad
        plt.figure(figsize=(10, 6))
        plt.hist(df['duracion'], bins=20, edgecolor='black')
        plt.xlabel('Duración (minutos)')
        plt.ylabel('Frecuencia')
        plt.title('Distribución de Frecuencia de la Duración de Actividades')
        plt.show()

        # Gráfico de Dispersión para la Relación Distancia/Duración
        plt.figure(figsize=(10, 6))
        plt.scatter(df['distancia'], df['duracion'])
        plt.xlabel('Distancia (km)')
        plt.ylabel('Duración (minutos)')
        plt.title('Relación Distancia/Duración de Actividades')
        plt.show()

        # Gráfico de Progreso en Objetivos (asumiendo que hay un DataFrame 'objetivos' con fechas y valores)
        objetivos = self.atleta.getObjetivos(correo_electronico)
        if objetivos:
            df_objetivos = pd.DataFrame(objetivos)
            df_objetivos['fecha'] = pd.to_datetime(df_objetivos['fecha'])

            plt.figure(figsize=(12, 6))
            plt.plot(df_objetivos['fecha'], df_objetivos['valor_objetivo'], marker='o')
            plt.xlabel('Fecha')
            plt.ylabel('Valor del Objetivo')
            plt.title('Progreso en Objetivos')
            plt.show()       

            
    

            


            
    
