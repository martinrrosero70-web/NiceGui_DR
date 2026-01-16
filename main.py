from difflib import restore
from nicegui import ui

# Funciones
def sumar():
    n1 =float(num1.value)
    n2 =float(num2.value)
    res = n1 + n2  
    resultado.set_text(f"resultado: {res}")

def restar():
    n1 =float(num1.value)
    n2 =float(num2.value)
    res = n1 - n2  
    resultado.set_text(f"resultado: {res}")  

# Estructuras de la interfaz de usuario
with ui.card().classes("w-60 m-auto p-4"):
    ui.label("cALCULADORA").classes("font-serif w-full text-center")
    num1 = ui.input("numero 1").classes("w-full")
    num2 = ui.input("numero 2").classes("w-full")
    bt_sumar = ui.button("SUMAR").classes("w-full bg-bleu-500 text-white").on ("click", sumar)
    bt_restar = ui.button("restar").classes("w-full bg-bleu-500 text-white").on ("click", restar)
    resultado = ui.label("resultado: ").classes("w-full text-center mt-4 ")

    ui.run()