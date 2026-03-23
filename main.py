"""
Ejercicio 1: 
Al ingresar un numero par cualquiera que sea del 2 al 100, este imprima en pantalla todos los  
números pares siguientes, y si ingreso un número impar cualquiera sea del 1 al 99 se imprima en  
pantalla todos los números impares siguientes hasta el 99. 
"""
#declaración
impares = []
pares = []

# aqui lleno los pares e impares
for p in range(1,101):
    if(p%2==0):
        pares.append(p)
    else:   
        impares.append(p)
    
#funciones
def imprimir_lista(numero_ingresado):
    lista_final = []
    if(numero_ingresado%2==0):
        numero_encontrado = False
        for p in pares:
            if(numero_encontrado):
                lista_final.append(p)
            else:
                if(numero_ingresado==p):
                    numero_encontrado=True
                    #lista_final.append(p)
        print(f"En número ingresado fue {numero_ingresado}, los pares siguentes son: ")
        print(lista_final)
    else:
        numero_encontrado = False
        for p in impares:
            if(numero_encontrado):
                lista_final.append(p)
            else:
                if(numero_ingresado==p):
                    numero_encontrado=True
                    #lista_final.append(p)
        print(f"En número ingresado fue {numero_ingresado}, los impares siguentes son: ")
        print(lista_final)

#main
while True:
    try:
        numero = int(input("Ingrese un número del 1 al 100: "))
        if(numero<=100 and numero>=1):
            imprimir_lista(numero)
            break
        else:
            print("Ese número está fuera del rango solicitado...")
    except ValueError:
        print("Error: eso no es un número.")

