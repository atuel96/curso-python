import PySimpleGUI as sg

# Definir el diseño de la ventana
layout = [
    [sg.Text("¡Hola, PySimpleGUI!")],  # Texto en la ventana
    [sg.Button("Presioname")]  # Botón
]

# Crear la ventana
window = sg.Window("Ventana con Botón", layout)

# Bucle de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:  # Cerrar la ventana
        break
    elif event == "Presioname":
        sg.popup("¡Botón presionado!")  # Muestra un mensaje emergente

# Cerrar la ventana
window.close()
