Algoritmo sin_titulo
	// Solicitar 3 notas y promediarlas
	// mostrar si aprobo o reprobo la asignara
	// validar si las notas entregadas estan en el rango de 10 a 70
	Definir nota1 Como Entero
	Definir nota2 Como Entero
	Definir nota3 Como Entero
	Definir promedio Como Real
	
	Escribir "Ingrese nota 1:"
	Leer nota1
	Escribir "Ingrese nota 2:"
	Leer nota2
	Escribir "Ingrese nota 3:"
	Leer nota3
	
	si nota1 >= 10 y nota1 <= 70 y nota2 >= 10 y nota2 <= 70 y  nota3 >= 10 y nota3 <= 70 Entonces
		promedio = (nota1 + nota2 + nota3) / 3
		si promedio >= 40 Entonces
			Escribir "Asignatura aprobada"
		SiNo
			Escribir "Asignatra reprobada"
		FinSi
	SiNo
		Escribir "Existe notas fuera del rango valido"
	FinSi
	
	
FinAlgoritmo
