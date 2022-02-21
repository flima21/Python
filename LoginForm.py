#===============================================================================================
# 2022.02.08 - LoginForm.py
# FELIPE PEDROSO DE LIMA
#===============================================================================================

"""
The script have a goal to simulate a login screen that order to user the login and password, if both match the user is in else not
"""
import PySimpleGUI as sg
import hashlib as md5
import pandas as pd

class LoginForm():
    def __init__(self):
        
        layout = [
            [sg.Text('Usuário'),sg.Input()],
            [sg.Text('Senha'  ),sg.Input()],
            [sg.Button('Login')                                         ]
        ]

        window = sg.Window('nm_sistema',size=(1000, 500)).layout(layout)
        # Here we can connect to database or create some array with values
        # Array
        vet = {
            "nm_user":[
                "Administrador",
                "Felipe Lima",
                "Larissa Gabriele",
                "Suporte",
                "Rodrigo Reis"
            ],
            "nm_login":[
                "admin",
                "flima",
                "lgabriele",
                "sup",
                "rreis"
            ],
            "nm_password":[
                "202cb962ac59075b964b07152d234b70",
                "202cb962ac59075b964b07152d234b70",
                "202cb962ac59075b964b07152d234b70",
                "202cb962ac59075b964b07152d234b70",
                "202cb962ac59075b964b07152d234b70",
            ]
        }

        df = pd.DataFrame(data=vet)
        

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            
            # If user press the button Login
            if event == "Login":
                pass_inform = values[1].encode()

                md5_senha = md5.md5(pass_inform)

                #Verify if the user and the password match
                if len(df.loc[(df['nm_login'] == values[0]) & (df['nm_password'] == md5_senha.hexdigest())]) == 1:
                    sg.Popup("You're in")
                else:
                    sg.PopupError('Password incorret')
        

tela = LoginForm()
tela.close()
