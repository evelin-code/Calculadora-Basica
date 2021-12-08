from tkinter import *

class Funciones: 

    operaciones = []
    numero = ""
    i = 0

    def __init__(self, var1):
        self.var1 = var1


    def validaOperaciones(self, n):
        self.mostrar(self.i, n)
        self.i += 1

        if not(n == "*" or n == "/" or n == "+" or n == "-" or n == "="):
            self.numero += n
            return False
        else:
            if self.numero != "":
                self.operaciones.append(self.numero)
            self.operaciones.append(n)
            self.numero = ""
            return True


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


    def mostrar(self, caracter, valor):
        self.var1.insert(caracter, valor)

    
    def calcula(self, num1, num2, operador):
        result = 0
        index = self.operaciones.index(operador)

        if operador == "*":
            result = num1 * num2
        elif operador == "/":
            result = num1 / num2
        elif operador == "+":
            result = num1 + num2
        else:
            result = num1 - num2
        
        self.operaciones[index] = result
        del self.operaciones[index-1]
        del self.operaciones[index]
        self.limpiar()
        self.mostrar(0, result)

    
    def obtenerNumeros(self, operador, opcion):
        if opcion == 1:
            return int(self.operaciones.__getitem__(self.operaciones.index(operador)-1))
        else:
            return int(self.operaciones.__getitem__(self.operaciones.index(operador)+1))


    def operacion(self, n):
        sn = self.validaOperaciones(n)
        
        if sn:
            if self.operaciones.__contains__("="):
                del self.operaciones[self.operaciones.index("=")]
                for i in self.operaciones:              
                    if self.operaciones.__contains__("*"):
                        num1 = self.obtenerNumeros("*", 1)
                        num2 = self.obtenerNumeros("*", 2)
                        self.calcula(num1, num2, "*")
                    elif self.operaciones.__contains__("/"):
                        try:
                            num1 = self.obtenerNumeros("/", 1)
                            num2 = self.obtenerNumeros("/", 2)
                            self.calcula(num1, num2, "/")
                        except:
                            self.limpiar()
                            self.mostrar(0, "No me exija dividir por 0")
                            break
                    elif self.operaciones.__contains__("+"): 
                        num1 = self.obtenerNumeros("+", 1)
                        num2 = self.obtenerNumeros("+", 2)
                        self.calcula(num1, num2, "+")
                    elif self.operaciones.__contains__("-"):
                        num1 = self.obtenerNumeros("-", 1)
                        num2 = self.obtenerNumeros("-", 2)
                        self.calcula(num1, num2, "-")
