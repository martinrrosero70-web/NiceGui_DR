from difflib import restore#se usa para comparar secuencias, pero no se utiliza en el código.
from nicegui import ui  # Importa la biblioteca NiceGUI para crear interfaces de usuario web con Python.

# Funciones
def sumar(): #realiza la suma de dos numeros 
    n1 =float(num1.value)
    n2 =float(num2.value)
    res = n1 + n2  
    resultado.set_text(f"resultado: {res}")

def restar(): #realiza la resta de 2 numeros
    n1 =float(num1.value)
    n2 =float(num2.value)
    res = n1 - n2  
    resultado.set_text(f"resultado: {res}")  

def multiplicar(): #realiza la resta de 2 numeros
    n1 =float(num1.value)
    n2 =float(num2.value)
    multiplcacion = n1 * n2  
    resultado.set_text(f"resultado: {multiplicardo}")

def dividir(): #realiza la resta de 2 numeros
    n1 =float(num1.value)
    n2 =float(num2.value)
    if n2 != 0:
        dividir = n1 / n2  
        resultado.set_text(f"resultado: {dividir}") 
    else:
        resultado.set_text("error : dividir por cero") 



# Estructuras de la interfaz de usuario
with ui.card().classes("w-60 m-auto p-4"): #crea una tarjeta centrada con un ancho de 60 unidades, marguen automatico. 
    ui.label("CALCULADORA").classes("font-serif w-full text-center")
    with ui.column().classes("w-full items-center"):
        num1 = ui.input("numero 1").classes("w-full")
        num2 = ui.input("numero 2").classes("w-full")
    with ui.row().classes("w-full mt-4 gap-2"):
        bt_sumar = ui.button("SUMAR").classes("w-full bg-blue-500 text-white").on ("click", sumar)
        bt_restar = ui.button("restar").classes("w-full bg-blue-500 text-white").on ("click", restar)
    with ui.row().classes("w-full mt-2 gap-2"):
        bt_multiplicar = ui.button("MULTPLICAR").classes(" bg-yellow-500 text-white flex-1").on("click", multiplicar)
        bt_dividir = ui.button("DIVIDIR").classes("bg-red-500 text-white flex-1").on("click", dividir)
    resultado = ui.label("resultado: ").classes("w-full text-center mt-4 ")

    ui.run()