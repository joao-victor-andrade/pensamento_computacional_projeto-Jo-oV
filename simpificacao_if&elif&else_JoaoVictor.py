print("Qual a sua idade?")


idade = int(input())

if idade <= 18:
    print('Você é menor de idade')

elif idade <= 60:
    print('Você é um adulto')

else:
    print('Você é idoso')