import requests

def clima():
    swapi = requests.get("https://swapi.dev/api/planets/")
    datos = swapi.json()
    planetarido = [planeta for planeta in datos["results"] if "arid" in planeta["climate"]]
    cont = len(planetarido)
    print(f"\nCANTIDAD DE PELICULAS EN EL QUE APARECEN PLANETAS CON CLIMA ARIDO: {cont}.")


def wookiee():
    swapi = requests.get("https://swapi.dev/api/films/3/")
    datos = swapi.json()
    wookiees = [person for person in datos["characters"] if "Wookiee" in person]
    cont = len(wookiees)
    print(f"\nCANTIDAD DE WOOKIEES QUE APARECEN EN LA SEXTA PELICULA: {cont}.")


def naves():
    swapi = requests.get("https://swapi.dev/api/starships/")
    datos = swapi.json()
    tamano = max(datos["results"], key=lambda x: int(x["length"]) if x["length"].isnumeric() else 0)
    navegra = tamano["name"]
    print(f"\nAEREONAVE MAS GRANDE DE LA SAGA: {navegra}")


while True:
    print("\n\nPreguntas")
    print("a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?")
    print("b) ¿Cuántos Wookies aparecen en la sexta película?")
    print("c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?")
    print("d) SALIR")
    opcion = input("Escoga una opcion: ").lower()

    if opcion == 'a':
        clima()
    elif opcion == 'b':
        wookiee()
    elif opcion == 'c':
        naves()
    elif opcion == 'd':
        break
    else:
        print("\nNO EXISTE ESA OPCION. INTENTE CON OTRA")

