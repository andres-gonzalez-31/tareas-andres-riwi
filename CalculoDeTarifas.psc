
Algoritmo CalculoDeTarifas
Definir opcionDia Como Entero
Definir horasTrabajadas Como Entero
Definir tarifa Como Entero
Definir esValido Como Logico

// Validaci�n para d�a laborable
Repetir
	Escribir "�Es d�a laborable?"
	Escribir "1. S�"
	Escribir "2. No"
	Leer opcionDia
	
	esValido <- (opcionDia = 1) O (opcionDia = 2)
	
	Si esValido = Falso Entonces
		Escribir "Error: Debe ingresar 1 o 2"
	FinSi
Hasta Que esValido = Verdadero

// Proceso seg�n opci�n
Si opcionDia = 2 Entonces
	Escribir "FIN DE SEMANA"
	Escribir "Tarifa: $0"
Sino
	// Validaci�n para horas trabajadas
	Repetir
		Escribir "Ingrese horas trabajadas (1-24):"
		Leer horasTrabajadas
		
		esValido <- (horasTrabajadas >= 1) Y (horasTrabajadas <= 24)
		
		Si esValido = Falso Entonces
			Escribir "Error: Ingrese entre 1 y 24 horas"
		FinSi
	Hasta Que esValido = Verdadero
	
	// C�lculo de tarifa
	Si (horasTrabajadas >= 7 Y horasTrabajadas <= 9) O (horasTrabajadas >= 17 Y horasTrabajadas <= 19) Entonces
		tarifa <- horasTrabajadas * 7
		Escribir "Horas PICO - Total a pagar: $", tarifa
	Sino
		tarifa <- horasTrabajadas * 5
		Escribir "Horas NORMALES - Total a pagar: $", tarifa
	FinSi
FinSi
FinAlgoritmo


