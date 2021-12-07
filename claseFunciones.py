#from InterfazCalculadora import *
from tkinter import *
class Funciones:

    def __init__(self, var1):
        self.var1 = var1
        print(self.var1)

    #Función para obtener el número del botón
    i = 0
    def obtenerNumeros(self, n):
        global i
        self.var1.insert(self.i, n)
        self.i+=1

    #Función para obtener el operador
    def obtenerOperadores(self, operador):
        global i
        self.var1.insert(self.i, operador)
        self.i+=1

    #Limpiar la pantalla
    def limpiar(self):
        self.var1.delete(0, END)

    #Limpiar de uno en uno los elementos
    def undo(self):
        self.var1_state = self.var1.get()
        if len(self.var1_state):
            var1_new_state = self.var1_state[:-1]
            self.limpiar()
            self.var1.insert(0, var1_new_state)
        else:
            self.limpiar()
            self.var1.insert(0, 'Error')

    #Símbolo del igual
    def calcular(self):
        pass

    #Suma
    def SumaP(self, numero1, numero2):
        sumaP = numero1 + numero2
        return sumaP

    #Resta
    def RestaP(self, numero1, numero2):
        restaP = numero1 - numero2
        return restaP

    #Division
    def DivisionP(self, numero1, numero2):
        try:
            divisionP = numero1 / numero2
            print("La division es ",divisionP)
        except ZeroDivisionError:
            print("Error! ZeroDivisionError")

    #Multiplicación
    def MultiplicacionP(self, numero1, numero2):
        multiP = numero1 * numero2
        print("La multiplicacion es ",multiP)