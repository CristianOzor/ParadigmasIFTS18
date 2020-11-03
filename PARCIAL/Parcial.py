import csv
import os.path

def menu():
    
    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")
		
        if opcion == "3":
            exit()
        if opcion == "1":
            guatdar_datos(empleados, fechas)
        if opcion == "2":
            cargar_datos(empleados)
        else:
            print("Por favor elija una opcion valida")

def guardar_datos(empleados, fechas):
	
	empleado_F = open(empleados)
    fechas_F = open(fechas)
    empleados_csv = csv.reader(empleado_F)
    dias_csv = csv.reader(fechas_F)
    
    #Salteo los encabezados de los archivos
    next(empleados_csv)
    next(dias_csv)
    
    # Empieza a leer
	empleado = next(empleados_csv, None)
	dias = next(dias_csv, None)
	
	While(empleado):
		
		
	# Cierro los archivos
    empleado_F.close()
    fechas_F.close()
		
def cargar_datos(archivo):
	pass

guardar_datos("empleados.csv", "dias.csv")
    
		
	
