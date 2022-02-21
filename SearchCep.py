#===============================================================================================
# 2022.02.08 - CONSULTA DE CEP COM JANELA
# FELIPE PEDROSO DE LIMA
#===============================================================================================
import PySimpleGUI as sg
import requests
import json
#===============================================================================================
# WindowCep: Define the class
#===============================================================================================
class WindowCep():
    def __init__(self):
        layout = [
          [sg.Text('CEP'),sg.Input()],
          [sg.Button('Procurar')]
        ]

        # Construct the window 
        window = sg.Window('CEP').layout(layout)

        #Get the values of the cep
        self.button,self.values = window.Read()

    # Allow to print the result
    def getCEP(self):
        cep = self.values[0]
        cep = cep.replace('-','')

        if len(cep) == 8:
          request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

          dados = json.loads(request.content)

          print('CEP: '       ,dados['cep']                       )
          print('Logradouro: ',dados['logradouro']                )
          print('Bairro: '    ,dados['bairro']                    )
          print('Localidade: ',dados['localidade']+'/'+dados['uf'])
          
        else:
          return False
          
tela = WindowCep()
tela.getCEP()
