from tkinter import *
class Funciones: 

    operaciones = []
    numero = ""
    i = 0

    def __init__(self, var1):
        self.var1 = var1

    def operar(self, n):
        sn = self.mostrar(n)
        result = 0

        if sn:
            print(self.operaciones)

            if(len(self.operaciones) > 2):
                if self.operaciones.__contains__("="):
                    del self.operaciones[self.operaciones.index("=")]
                    for i in self.operaciones:
                        # ["5", "+", "2", "*", "3", "*", "4"] = 29
                        # ["10", "/", "2", "+", "4"] =  9                 
                        if self.operaciones.__contains__("*"):
                            result = int(self.operaciones.__getitem__(self.operaciones.index("*")-1)) * int(self.operaciones.__getitem__(self.operaciones.index("*")+1))
                            index = self.operaciones.index("*")
                            self.operaciones[index] = result
                            del self.operaciones[index-1]
                            del self.operaciones[index]
                            self.limpiar()
                            self.var1.insert(0, result)
                        elif self.operaciones.__contains__("/"):
                            try:
                                result = int(self.operaciones.__getitem__(self.operaciones.index("/")-1)) / int(self.operaciones.__getitem__(self.operaciones.index("/")+1))
                                index = self.operaciones.index("/")
                                self.operaciones[index] = result
                                del self.operaciones[index-1]
                                del self.operaciones[index]
                                self.limpiar()
                                self.var1.insert(0, result)
                            except:
                                self.limpiar()
                                self.var1.insert(0, "No me exija dividir por 0")
                                break
                        elif self.operaciones.__contains__("+"): 
                            result = int(self.operaciones.__getitem__(self.operaciones.index("+")-1)) + int(self.operaciones.__getitem__(self.operaciones.index("+")+1))
                            index = self.operaciones.index("+")
                            self.operaciones[index] = result
                            del self.operaciones[index-1]
                            del self.operaciones[index]
                            self.limpiar()
                            self.var1.insert(0, result)
                        elif self.operaciones.__contains__("-"):
                            result = int(self.operaciones.__getitem__(self.operaciones.index("-")-1)) - int(self.operaciones.__getitem__(self.operaciones.index("-")+1))
                            index = self.operaciones.index("-")
                            self.operaciones[index] = result
                            del self.operaciones[index-1]
                            del self.operaciones[index]
                            self.limpiar()
                            self.var1.insert(0, result)

            print(self.operaciones)
    
    def mostrar(self, n):
        self.var1.insert(self.i, n)
        self.i += 1

        if not(n == "*" or n == "/" or n == "+" or n == "-" or n == "="):
            self.numero += n
            return False
        else:
            self.operaciones.append(self.numero)
            self.operaciones.append(n)
            self.numero = ""
            return True
            
    #Función para obtener el número del botón
    def obtenerNumeros(self, n):
        global i
        self.var1.insert(self.i, n)
        self.numero += n
        self.operaciones.append(self.numero)
        self.i+=1

    #Función para obtener el operador
    def obtenerOperadores(self, operador):
        global i
        # if operador == "+":
        #     self.limpiar()
        #     self.var1.insert(0, self.sumaP(self.numero))
        #     self.numero=""
        # elif operador == "-":
        #     self.limpiar()
        #     self.var1.insert(0, self.restaP(self.numero))
        #     self.numero=""

        self.var1.insert(self.i, operador)
        self.operaciones.append(operador)
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