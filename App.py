from Clase import *
from time import sleep
#from graphviz import Source
import os

lista_peliculas = []
lista_actores = []
lista_anios = []
lista_generos = []

str_inicial = """------LENGUAJES FORMALES DE PROGRAMACION------
*               Sección: A-                 *
*              Carnet: 202100259            *   
*   Nombre: Jonathan Josue Alvarez Chacon   *
----------------------------------------------"""

str_menu_principal ="""---------Menu Principal---------
* 1.Cargar Archivo            *
* 2.Gestionar Películas       *
* 3.Filtrado                  *
* 4.Grafica                   *
* 5.Salir                     *
--------------------------------"""

str_menu_gestionar ="""-----------Gestion de Peliculas-----------
* 1.Ver peliculas                  *
* 2.Ver actores                    *
-----------------------------------------"""

str_menu_filtrado = """-------Filtrar-------
* 1. Actor     *
* 2. Año       *
* 3. Género    *
----------------------"""

def cls():
    os.system('cls')  

def Cargar_archivo():
    cls()
    try:
        ruta = input("Escriba la direccion de entrada: ")
        f = open(ruta,"r")
        
        str_entrada = f.read()
        filas = str_entrada.split("\n")
        for fila in filas:
            partes = fila.split(";")
            nombre = partes[0].strip()
            actores = partes[1].split(",")
            anio = partes[2].strip()
            genero = partes[3].strip()

            for i in range(len(actores)):
                actores[i] = actores[i].strip()
                actor = actores[i]
                if actor not in lista_actores:
                    lista_actores.append(actor)

            if anio not in lista_anios:
                lista_anios.append(anio)

            if genero not in lista_generos:
                lista_generos.append(genero)
                    
            lista_peliculas.append(Pelicula(nombre,actores,anio,genero))
        print("Se ha cargado el archivo con exito")
        sleep(2)

    except:
        print("ERROR No se pudo cargar el archivo")
        sleep(2)

def Gestionar():
    cls()
    print(str_menu_gestionar)
    eleccion = input("Elige una Opcion: ")
    if eleccion == "1":
        Mostrar_peliculas()
    elif eleccion == "2":
        Mostrar_actores()
    else:
        print("ERROR seleccion no valida!")
        sleep(2)

def Mostrar_peliculas():
    cls()
    print("--------------Peliculas--------------")
    for pelicula in lista_peliculas:
        print("Nombre: ",pelicula.nombre)
        print("Año: ", pelicula.anio)
        print("Genero: ", pelicula.genero)
        print("*************************************")
    input()


def Mostrar_actores():
    seleccion = "1245"
    while True:
        cls()
        print("--------------Seleccion de pelicula--------------")
        for pelicula in lista_peliculas:
            print(str(lista_peliculas.index(pelicula)+1)+".- "+pelicula.nombre)
        print(str(len(lista_peliculas)+1)+".- Salir")
        print("**************************************************")
        while True:
            try:
                seleccion = int(input("Selecciona una pelicula: "))-1
                break
            except:
                print("La entrada debe ser un numero")

        if seleccion == len(lista_peliculas):
            return None
            
        if abs(seleccion) > len(lista_peliculas):
            print("Seleccion no valida!!")
            sleep(2)
            continue
        
        pelicula_seleccionada = lista_peliculas[seleccion]
        cls()
        print("Actores en "+pelicula_seleccionada.nombre+": ")
        for actor in pelicula_seleccionada.actores:
            print(" "+str(pelicula_seleccionada.actores.index(actor)+1)+".- "+actor)
        input()


def Filtrado():
    cls()
    print(str_menu_filtrado)
    eleccion = input("Selecciona una Opcion: ")
    if eleccion == "1":
        Filtrado_por_actor()
    elif eleccion == "2":
        Filtrado_por_anio()
    elif eleccion == "3":
        Filtrado_por_genero()
    else:
        print("ERROR seleccion no valida!!")
        sleep(2)

def Filtrado_por_actor():
    cls()
    print("--------------Seleccion de Actor--------------")
    for actor in lista_actores:
        print(str(lista_actores.index(actor)+1)+".- "+actor)
    print("************************************************")
    while True:
        try:
            seleccion = int(input("Selecciona un autor: "))-1
            break
        except:
            print("Ingresa un numero!")
        
    if abs(seleccion) >= len(lista_actores):
        print("Seleccion no valida!!")
        return
    
    actor_seleccionado = lista_actores[seleccion]
    cls()
    print("Peliculas del actor "+actor_seleccionado+": ")

    for pelicula in lista_peliculas:
        if actor_seleccionado in pelicula.actores:
            print(" Nombre: ",pelicula.nombre)
            print(" Año: ", pelicula.anio)
            print(" Genero: ", pelicula.genero)
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    input()


    
def Filtrado_por_anio():
    cls()
    print("--------------Seleccion de Año--------------")
    for anio in lista_anios:
        print(str(lista_anios.index(anio)+1)+".- "+anio)
    print("***********************************************")
    while True:
        try:
            seleccion = int(input("Selecciona un año: "))-1
            break
        except:
            print("Solo se pueden ingresar numeros!")
        
    if abs(seleccion) >= len(lista_anios):
        print("Seleccion no valida!!")
        return
    
    anio_seleccionado = lista_anios[seleccion]
    cls()
    print("Peliculas publicadas en el año "+anio_seleccionado+": ")
    
    for pelicula in lista_peliculas:
        if pelicula.anio == anio_seleccionado:
            print(" Nombre: ",pelicula.nombre)
            print(" Año: ", pelicula.anio)
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            
    input()


def Filtrado_por_genero():
    cls()
    print("--------------Seleccion de género--------------")
    for genero in lista_generos:
        print(str(lista_generos.index(genero)+1)+".- "+genero)
    print("***********************************************")
    while True:
        try:
            seleccion = int(input("Selecciona un género: "))-1
            break
        except:
            print("Solo se aceptan numeros!")
        
    if abs(seleccion) >= len(lista_generos):
        print("Seleccion no valida!!")
        return
    
    genero_seleccionado = lista_generos[seleccion]
    cls()
    print("Peliculas con el género "+genero_seleccionado+": ")
    
    for pelicula in lista_peliculas:
        if pelicula.genero == genero_seleccionado:
            print(" Nombre: ",pelicula.nombre)
            print(" Genero: ", pelicula.genero)
            print("-------------------------------------")
    
    input()



print(str_inicial)
input()
seleccion_mp = "s"

while seleccion_mp != "5":
    cls()
    print(str_menu_principal)
    seleccion_mp = input("Elige una opcion: ")
    if seleccion_mp == "1":
        Cargar_archivo()
    elif seleccion_mp == "2":
        Gestionar()
    elif seleccion_mp == "3":
        Filtrado()
    elif seleccion_mp == "4":
        print("No me salió :(")
        sleep(2)
    elif seleccion_mp == "5":
        print("HASTA LUEGO!")
        continue
    else:
        print("Seleccion no valida!")
        sleep(2)
