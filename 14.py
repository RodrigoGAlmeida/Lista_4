#Recebe um numero inteiro e verifica se é numero primo
numero = int(input("Digite um numero inteiro: "))
primo = True
if numero <= 1:
    print(numero, "não é um numero primo")
else:
    for i in range(2,numero):
        if numero % i == 0:
            primo = False

if primo:
    print(numero, "É um numero primo!")
else: 
    print(numero, "Não é um numero primo!")
