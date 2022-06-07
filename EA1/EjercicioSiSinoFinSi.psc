Algoritmo EjercicioSiSinoFinSi
	Definir sueldoTrabajador1 Como Entero
	Definir sueldoTrabajador2 Como Entero
	Definir sueldoTrabajador3 Como Entero
	
	Escribir "Ingrese el 1er sueldo"
	Leer sueldoTrabajador1
	Escribir "Ingrese el 2do sueldo"
	Leer sueldoTrabajador2
	Escribir "Ingrese el 3er sueldo"
	Leer sueldoTrabajador3
	
	si sueldoTrabajador1 > sueldoTrabajador2 Entonces
		si sueldoTrabajador1 > sueldoTrabajador3 Entonces
			Escribir "El trabajador 1 tiene el mayor sueldo"
		sino
			Escribir "El trabajador 3 tiene el mayor sueldo"
		FinSi
	SiNo
		si sueldoTrabajador2 > sueldoTrabajador3 Entonces
			Escribir "El trabajador 2 tiene el mayor sueldo"
		sino
			Escribir "El trabajador 3 tiene el mayor sueldo"
		FinSi
	FinSi
	
	
	
FinAlgoritmo
