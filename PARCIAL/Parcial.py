import csv
import os.path

def menu():
    #Ciclo que itera hasta que 
    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")
		
        if opcion == "3":
            exit()
        if opcion == "1":
            eje7_guardar(ARCHIVO, CAMPOS)
        if opcion == "2":
            eje7_cargar(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")

def guardar_datos(empleados, fechas)
	pass

def cargar_datos()
	pass
