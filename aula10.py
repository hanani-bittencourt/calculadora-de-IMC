#exercicio
# nome = 'Hanani Bittencourt'
# altura = 1.80
# peso = 90
# imc = peso / altura **2

# print(nome, 'tem', altura, 'de altura,',)
# print('pesa', peso, 'quilos e seu imc é,',)
# print(imc)
import time
#calculadora IMC
print('Bem-vindo a minha calculadora de IMC') 
time.sleep(5)
print('===============Calcule=====================')
nome_paciente = input('Qual é o seu nome? ')
time.sleep(2)
nome = ("Ola", nome_paciente)
idade = input(f'Qual sua idade?')
time.sleep(2)
peso = float(input('Qual é o seu peso (em KG)?'))
time.sleep(2)
altura = float(input('Qual sua altura(em metros e usando ponto)?'))
time.sleep(2)
print('Vamos calcular seu IMC')

imc = (peso / (altura * altura))

print(nome_paciente, (f'seu IMC é: {imc:.3f}'))

if imc < 16:
    print('Seu estado é de Magreza grave/nProcure um médico ou nutricionista.')
elif imc < 17:
    print('Seu estado é de Magreza moderada\nPrecisa rever sua alimentação.')
elif imc < 18.5:
    print('Seu estado é de Magreza leve\nPrecisa rever sua alimentação.')
elif imc < 25:
    print('Voce está Saudável\nParabéns!.')
elif imc < 30:
    print('Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.')
elif imc < 35:
    print('Seu estado é de Obesidade Grau 1\n Procure um médico ou nutricionista.')
elif imc < 40:
    print('Seu estado é de Obesidade Grau 2 (SEVERA)\n Procure um médico ou nutricionista.')      
else:
 print('Seu estado é de Obesidade grau 3 (mórbida)\nProcure um médico ou nutricionista')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         