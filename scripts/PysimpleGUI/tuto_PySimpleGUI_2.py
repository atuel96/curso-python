import PySimpleGUI as sg

layout = [
    [sg.Text("Escribe algo:"), sg.InputText(key="input")],
    [sg.Button("Mostrar"), sg.Button("Salir")]
]
window = sg.Window("Ventana con Entrada", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break
    elif event == "Mostrar":
        sg.popup(f"Escribiste: {values['input']}")
        
window.close()

