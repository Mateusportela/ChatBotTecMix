import os
def processar_resposta(resposta,nome):
 if resposta == '1':
  print(f'{os.linesep}{nome} Temos 5 modelos: D20 PRO, IWO X8, IWO X8 Max, IWO W46 e IWO HW22 {os.linesep}')
 elif resposta == '2':
  print(f'{os.linesep}{nome} Vendemos! Temos o Lenovo LP40, Lenovo LP1, Y30, Y50 e o Airpods 2 {os.linesep}')
 elif resposta == '3':
  print(f'{os.linesep}{nome} D20 R$70,00; IWO X8 R$140,00; IWO X8 Max R$170,00; IWO W46 R$250,00; IWO HW22 R$280,00 {os.linesep}')
 elif resposta == '4':
  print(f'{os.linesep}{nome} Y50 custa R$70; Y30 custa R$70; Lenovo LP1 custa R$120,00; Lenovo LP40 custa R$115,00; Airpods 2 custa R$190,00 {os.linesep}') 
 else:
  print('Digite apenas 1,2,3 ou 4')
def start():
 #apresentar o chatbot
 print('olá! Bem vindo a TecMix Store')
 #pedir nome
 nome = input('Digite seu nome: ')
 #pedir email
 email = input('Digite seu e-mail: ')
 while True:
    #oferecer o menu de opções
    resposta = input(f'O que gostaria de saber dos nossos produtos?{os.linesep}[1] - Quais modelos de smartwatch voçês tem?{os.linesep}[2] - Voçês vendem fone TWS? Qual modelos?{os.linesep}[3] - Qual valor dos smartwatch?{os.linesep}[4] - Qual o valor dos fones TWS?{os.linesep}')
    #processar as respostas enviadas
    processar_resposta(resposta,nome)

start()