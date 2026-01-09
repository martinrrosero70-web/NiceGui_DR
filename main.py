from nicegui import ui

# Funciones


# Estructuras de la interfaz de usuario
with ui.card().classes("w-60 m-auto p-4"):
    ui.label("hola, mundo").classes("font-serif")


    ui.run()