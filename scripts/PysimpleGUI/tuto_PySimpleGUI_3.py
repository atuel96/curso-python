import PySimpleGUI as sg

# Función para crear la segunda ventana
def crear_nueva_ventana():
    # Diseño de la segunda ventana
    layout_nueva_ventana = [
        [sg.Text("Escribe algo en la nueva ventana:")],
        [sg.InputText(key="nuevo_input")],
        [sg.Button("Cerrar")]
    ]
    
    # Crear la segunda ventana
    nueva_ventana = sg.Window("Nueva Ventana", layout_nueva_ventana)
    
    # Bucle de eventos para la nueva ventana
    while True:
        event, values = nueva_ventana.read()
        if event == sg.WINDOW_CLOSED or event == "Cerrar":
            break
    
    nueva_ventana.close()

# Diseño de la ventana principal
layout_ventana_principal = [
    [sg.Text("Ventana Principal")],
    [sg.Button("Abrir nueva ventana")],
    [sg.Button("Salir")]
]

# Crear la ventana principal
ventana_principal = sg.Window("Ventana Principal", layout_ventana_principal)

# Bucle de eventos para la ventana principal
while True:
    event, values = ventana_principal.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break
    elif event == "Abrir nueva ventana":
        # Llamar a la función que abre la nueva ventana
        crear_nueva_ventana()

ventana_principal.close()
