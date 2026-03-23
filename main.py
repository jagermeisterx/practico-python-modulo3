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
        if(len(lista_final)==0):
            print("No quedan más pares siguientes")
        else:
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
        if(len(lista_final)==0):
            print("No quedan más impares siguientes")
        else:
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

"""
Ejercicio 2: 
Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre  0 y 10). 
A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado  y la menor. 

"""
notas = []
for i in range(1,6):
    while True:
        try:
            nota = int(input("Ingrese nota del 1 al 10: "))
            if(nota<0 or nota>10):
                print("Ingrese una nota válida: ")
            else:
                notas.append(nota)
                break
        except ValueError:
            print("Error, ingrese un número. ")
promedio = sum(notas)/len(notas)
nota_minima=min(notas)
nota_max=max(notas)

print(f"El promedio del estudiante es {promedio}, su nota mínima es {nota_minima} ; mientras su nota máxima es {nota_max}")

"""
Ejercicio 3: 
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga  cuántos días tiene (por ejemplo, 30) 
y el nombre del mes. Debes usar listas. Para simplificarlo vamos  a suponer que febrero tiene 28 días.  

"""
nombres_meses = [
    "Enero", "Febrero", "Marzo",     "Abril",   "Mayo",      "Junio",
    "Julio", "Agosto",  "Septiembre","Octubre",  "Noviembre", "Diciembre"
]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    try:
        indice=int(input("Ingrese número del mes deseado: "))
        if(indice<=12 and indice>=1):
            indice = indice - 1
            print(f"El número ingresado corresponde a {nombres_meses[indice]}, y ese mes tiene {dias_meses[indice]} días.")
            break
        else:
            print("Nota fuera del rango. ")
    except ValueError:
        print("Eso no es un número, intente de nuevo. ")