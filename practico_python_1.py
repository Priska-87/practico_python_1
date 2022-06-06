"""Función Suma: Priscila Kwiatkowski Aula 3"""

def suma (num1, num2, num3):
    resultado = num1 + num2 + num3
    return (resultado) 


#Función Resta(): Aaron Cortez 

def resta(a,b):
    return (a - b)


# producto : Eric diaz

def producto(numero_1,numero_2,numero_3,numero_4):
    return (numero_1*numero_2*numero_3*numero_4)

#imprimir : Aaron Cortez
def imprimir(texto,valor):
    print(texto,valor)


def programa():
    operacion = int(input("¿Que operacion desea realizar?\n1: Suma\n2: Resta\n3: Multiplicación\n"))
    if operacion == 1:
        num1= int(input("Ingrese un valor numérico: "))
        num2= int(input("Ingrese un valor numérico: "))
        num3= int(input("Ingrese un valor numérico: "))

        imprimir("el resultado es:",suma(num1,num2,num3))

    elif operacion == 2:
        a= int(input("Ingrese el primer numero: "))
        b= int(input("Ingrese el segundo numero: "))

        imprimir("el resultado de la resta es: ", resta(a,b))

    elif operacion == 3:
        print ("Ingresa cuatro números")
        numero_1 = int(input("Introduce tu primer número: "))
        numero_2 = int(input("Introduce tu segundo número: "))
        numero_3 = int(input("Introduce tu tercer número: "))
        numero_4 = int(input("Introduce tu cuarto número: "))

        mensaje = "RESULTADO: El producto de " + str(numero_1) + " * " + str(numero_2) + " * " + str(numero_3) + " * " + str(numero_4) + " es igual a: "

        imprimir(mensaje,producto(numero_1,numero_2,numero_3,numero_4))
    
    else:
        print("ingrese un valor valido: (1, 2 o 3)")
        reiniciar()

    nuevaOperacion = int(input("¿Desea realizar otra operación? :\n 1: Si\n 2: No\n"))

    if nuevaOperacion == 1:
        reiniciar()
    elif nuevaOperacion == 2:
        print("Usted a elegido No")
def reiniciar():
    programa()

programa()


