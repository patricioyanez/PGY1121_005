Algoritmo Angulos
	Definir angulo1 Como Entero
	Definir angulo2 Como Entero
	Definir angulo3 Como Entero
	Definir total Como Entero
	
	// solicitar datos
	Escribir "Ingrese primer angulo:"
	Leer angulo1
	Escribir "Ingrese segundo angulo:"
	Leer angulo2
	Escribir "Ingrese tercera angulo:"
	Leer angulo3
	
	// procesar
	total = angulo1 + angulo2 + angulo3
	
	si total <> 180 Entonces
		Escribir "Los angulos no suman 180"
	SiNo
		// equilatero
		si angulo1 = angulo2 y angulo1 = angulo3 Entonces
			Escribir "Es un triangulo equilatero"
		SiNo
			si angulo1 = angulo2 o angulo1 = angulo3 o angulo2 = angulo3 Entonces
				Escribir "Es un triangulo isoceles"
			SiNo
				Escribir "Es un triangulo escaleno"
			FinSi
		FinSi
		
		
	FinSi
	
FinAlgoritmo
