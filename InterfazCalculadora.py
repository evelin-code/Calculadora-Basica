from tkinter import *

root = Tk()
root.title("Calculadora")
root.resizable(0,0)
root.geometry("459x458+750+300")
root.config(background='#7A89C9')
var1 = Entry(root)
var1.grid(row=1, columnspan=6, sticky=W+E)
var1.config(font=("Calibri 16"))

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

# Botones de los números y signos

Button(root, text="1", width=15, height=5, command=lambda:obtenerNumeros(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", width=15, height=5, command=lambda:obtenerNumeros(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", width=15, height=5, command=lambda:obtenerNumeros(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", width=15, height=5, command=lambda:obtenerNumeros(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", width=15, height=5, command=lambda:obtenerNumeros(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", width=15, height=5, command=lambda:obtenerNumeros(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", width=15, height=5, command=lambda:obtenerNumeros(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", width=15, height=5, command=lambda:obtenerNumeros(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", width=15, height=5, command=lambda:obtenerNumeros(9)).grid(row=4, column=2, sticky=W+E)

Button(root, text="AC", width=15, height=5, command=lambda:limpiar()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", width=15, height=5, command=lambda:obtenerNumeros(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="←", width=15, height=5, command=lambda:undo()).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", width=15, height=5, command=lambda:obtenerOperadores("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", width=15, height=5, command=lambda:obtenerOperadores("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="/", width=15, height=5, command=lambda:obtenerOperadores("/")).grid(row=4, column=3, sticky=W+E)
Button(root, text="*", width=15, height=5, command=lambda:obtenerOperadores("*")).grid(row=5, column=3, sticky=W+E)

Button(root, text="=", width=15, height=5).grid(row=6, columnspan=6, sticky=W+E)

root.mainloop()