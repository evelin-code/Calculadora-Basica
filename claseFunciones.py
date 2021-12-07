from tkinter import *
class Funciones:

    numero = ""
    i = 0

    def __init__(self, var1):
        self.var1 = var1
        print(self.var1)

    #Función para obtener el número del botón
    def obtenerNumeros(self, n):
        global i
        self.var1.insert(self.i, n)
        self.numero+=n
        self.i+=1

    #Función para obtener el operador
    def obtenerOperadores(self, operador):
        global i
        if operador == "+":
            self.limpiar()
            self.var1.insert(0, self.sumaP(self.numero))
            self.numero=""
        elif operador == "-":
            self.limpiar()
            #print(type(self.numero))
            self.var1.insert(0, self.restaP(self.numero))
            self.numero=""
            print("hola")

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
    suma = 0
    def sumaP(self, numero1):
        self.suma += int(numero1)
        return self.suma

    #Resta
    resta = 0
    def restaP(self, numero1):
        self.resta -= int(numero1)
        return self.resta

    #Division
    def divisionP(self, numero1, numero2):
        try:
            divisionP = numero1 / numero2
            print("La division es ",divisionP)
        except ZeroDivisionError:
            print("Error! ZeroDivisionError")

    #Multiplicación
    def multiplicacionP(self, numero1, numero2):
        multiP = numero1 * numero2
        print("La multiplicacion es ",multiP)