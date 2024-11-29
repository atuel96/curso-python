import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
class interfaz:
    def __init__(self):
        sg.ChangeLookAndFeel('LightGreen')
        layout = [[sg.Text('Inicio de Sesion', size=(40, 1), justification='center')],
                  [sg.Text(text='Inicio de Sesion', justification='center')],
                  [sg.Text(text='Usuario')],
                  [sg.InputText()],
                  [sg.Text('Contraseña')],
                  [sg.InputText()],
                  [sg.Button('Iniciar Sesion', key='validar'), sg.Button('Cancelar', key = 'cancelar')]
                  ]
        self.window = sg.Window('Inicio de Sesion', location=(800, 400))
        self.window.Layout(layout).Finalize()
        while True:
            event, values = self.window.Read()
            if event == 'Exit' or event is None:
                sys.exit()
                break
            if event == 'validar':
                self.validar(values[0], values[1])
            if event == 'cancelar':
                sys.exit()
    def validar(self, usuario, contraseña):
        if usuario == 'usuario' and contraseña == 'contraseña':
            sg.Popup('Usuario Validado')
        else:
            sg.Popup('Usuario Incorrecto')
inter = interfaz()