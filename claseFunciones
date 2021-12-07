#from InterfazCalculadora import *

class Funciones:

    def __init__(self):
        pass

    #Función para obtener el número del botón
    i = 0
    def obtenerNumeros(n):
        global i
        var1.insert(i, n)
        i+=1

    #Función para obtener el operador
    def obtenerOperadores(operador):
        global i
        var1.insert(i, operador)
        i+=1

    #Limpiar la pantalla
    def limpiar():
        var1.delete(0, END)

    #Limpiar de uno en uno los elementos
    def undo():
        var1_state = var1.get()
        if len(var1_state):
            var1_new_state = var1_state[:-1]
            limpiar()
            var1.insert(0, var1_new_state)
        else:
            limpiar()
            var1.insert(0, 'Error')

    #Símbolo del igual
    def calcular():
        pass

    #Suma
    def SumaP(numero1, numero2):
        sumaP = numero1 + numero2
        return sumaP

    #Resta
    def RestaP(numero1, numero2):
        restaP = numero1 - numero2
        return restaP

    #Division
    def DivisionP(numero1, numero2):
        try:
            divisionP = numero1 / numero2
            print("La division es ",divisionP)
        except ZeroDivisionError:
            print("Error! ZeroDivisionError")

    #Multiplicación
    def MultiplicacionP(numero1, numero2):
        multiP = numero1 * numero2
        print("La multiplicacion es ",multiP)