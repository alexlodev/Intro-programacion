

## Array de datos:
# opciones = ['Cosa 1', 'Cosa 2', 'Cosa 3' ]

## Funciones        ## Lo que esta dentro de los parentisis se le llaman parametros
def nombreDeFuncion(nombre):
    ## Condicionales
    ## Comparar datos se utiliza == 
    if nombre == 'Andres':
        print('hola ' + nombre)
    elif nombre == 'Alexis':
        print('hola ', nombre)
    else: 
        print(':v')

## Invocar funcion:
# nombreDeFuncion(213)


# Tarea: Tratar de entender la siguiente logica:. #
import enquiries 

planetas = ['Júpiter', 'Venus', 'Urano', 'Marte', 'Mercurio', 'Saturno', 'Neptuno', 'Tierra']

# Dictionary 
diccionarioPlanetas = {'Júpiter': 2.55 , 'Venus' : 0.87 , 'Urano' : 0.99, 'Marte' : 0.38 , 'Mercurio' : 0.39, 'Saturno' : 0.93, 'Neptuno' : 1.38 , 'Tierra' : 1}

planetaSeleccionado = enquiries.choose(' Escoja el planeta: ', planetas)

pesoDelUsuario = float(input('Ingrese su peso: '))


def calcularPeso(planetaSeleccionado, pesoDelUsuario): 
    print('Usted pesa: ', diccionarioPlanetas[planetaSeleccionado] * pesoDelUsuario , 'en', planetaSeleccionado)


calcularPeso(planetaSeleccionado, pesoDelUsuario)
