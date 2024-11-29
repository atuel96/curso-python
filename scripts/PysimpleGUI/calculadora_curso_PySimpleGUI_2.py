import PySimpleGUI as sg

layout = [
    [sg.Text('Valor 1'), sg.InputText(key="val1")],
    [sg.Text('Valor 2'),sg.InputText(key="val2",size=(10,1))],
    [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],
    [sg.Text('Resultado'), sg.Text('', key='result')],
    [sg.Button('Salir')]
]

window = sg.Window('Calculadora', layout, margins=(10, 10))

while True:
    event, values = window.read()

    if event == '+':
        window["result"].update(float(values['val1']) + float(values['val2']))

    if event == '-':
        window["result"].update(float(values['val1']) - float(values['val2']))

    if event == '*':
        window["result"].update(float(values['val1']) * float(values['val2']))

    if event == '/':
        window["result"].update(float(values['val1']) / float(values['val2']))

    if event == "Salir" or event == sg.WIN_CLOSED:
        break

window.close()