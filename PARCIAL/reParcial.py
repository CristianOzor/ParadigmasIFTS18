import csv
import os.path

def upload_data(campos):
	employee_list = []
	exitUp = ''
	
	while exitUp != si:
		employee = {}
		
		for campo in campos:
			employee[campo] = input(f"Ingrese {campo} del empleado")
		
		employee_list.append(employee)
		
		exitUp = input("¿Desea seguir agregando registros? si/no").lower()
	
	return employee_list	
		
def save_data(data_file, campos):
	
	file_name = input("Ingrese un nombre con el que desee guardar al archivo ")
	file_name_final = (f"{file_name}.csv")
	
	#valida que si archivo no existe y crea uno nuevo
	if not (os.path.isfile(file_name_final)):
		
		
		try:
			with open(file_name_final, 'w', newline = '') as file:
				file_guarda = csv.DictWriter(file, fieldnames = campos)
				
				file_guarda.writeheader()
				file_guarda.writerows(data_file)
				
				print("Se creo el archivo exitosamente")
				return
				
		except IOError:
			print("Ocurrio un error al crear el archivo")
	
	#valida si el archivo existe
	if(os.path.isfile(file_name_final)):
		
		user_ask = input("¿Desea sobrescribir el archivo o modificarlo?: s/m").lower()
		
		if (user_ask == 's'):
		 
			try:
				with open(file_name_final, 'w+', newline = '') as file:
					file_guarda = csv.DictWriter(file, fieldnames = campos)
				
					file_guarda.writeheader()
					file_guarda.writerows(data_file)
					
					print("El archivo se sobrescribio correctamente")
					return
					
			except IOError:
				print("Ocurrio un error al sobrescribir el archivo")
		
		if (user_ask == 'm'):
			
			try:
				with open(archivo, 'a', newline='') as file:
					file_guarda = csv.DictWriter(file, fieldnames=campos)
					
					#si el archivo no existe le graba el encabezado de los campos
					if not archivo_existe:
						file_guarda.writeheader()

					file_guarda.writerows(data_file)
					
					print("se guardo correctamente la modificación")
					return
			
			except IOError:
				print("Ocurrio un error al modificar el archivo")




def load_data(archivo):
	with open (archivo, 'r', newline = '') as load:
		lectura_csv = csv.DictReader(load)
		campos = lectura_csv.fieldnames
		
		for linea in lectura_csv:
			print(linea\n)
	
	except IOError:
		print("Error al cargar el archivo")
	
	
def consult_data(empleados, dias):
	try:
		with open (empleados, 'r', newline = '') as file1, open (dias, 'r', newline = '') as file2:
			
			employee_csv = csv.reader(file1)
			days_csv = csv.reader(file2)
			
			#salteo los encabezados
			next(employee_csv)
			next(days_csv)
			
			#empiezo a leer
			employee= next(employee_csv, None)
			vacation= next(days_csv, None)
			
						
			while (employee):
				legajo, apellido, nombre, vacaciones = employee
				try:
					vacaciones = int(vacaciones)
				except ValueError:
					print("El valor no es un numero entero")
				
				dias_tomados = 0
				while(vacation and vacation[0] == legajo):
					dias_tomados +=1
					vacation= next(days_csv, None)
				
			
					
		
	except IOError:
		print("hubo un error en la lectura")

def menu():
    
    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            upload_data(CAMPOS)
        if opcion == "2":
            eje7_cargar(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")
