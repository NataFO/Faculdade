from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
credcarb= 5


layout= [ 
    [sg.Text('Cálculo de Crédito de Carbono')],
    [sg.Text('Olá, seja bem-vindo(a) ao sistema de Conversão de Créditos de Carbono! \nInsira os dados a seguir para fazer os cálculos.')],
    [sg.Text('Digite o total de hectares queimados em seu país no último ano:'), (sg.Input(key='queimadas'))],
    [sg.Text('Digite o total de hectares desmatados em seu país no último ano:'), sg.Input(key='desmatamento')],
    [sg.Text('Digite o total de toneladas de CO2 gerado por combustíveis fósseis:'), sg.Input(key='combfossil')],
    [sg.Button('Calcular')],
]

janela=sg.Window("Cálculo do Crédito de Carbono", layout,size=(2000, 800))

cq=0
cd=0

while True:
    event, values = janela.read()
    #print(event, values)
    
    cq=float(values['queimadas']) * 30
    cd=float(values['desmatamento']) * 30
    cc=float(values['combfossil'])
    cred= cq + cd +  cc
    lucro= cred * 5


    if event == "Calcular":
        sg.popup(f'O seu total de créditos de carbono é {cred:,.2f}')
        sg.popup(f'O seu lucro com a venda dos créditos é de {lucro:,.2f} doláres')

    if event == sg.WIN_CLOSED:
        break

