#Mostre os numeros primos entre 1 e N e o numero de divisões feitas
num=int(input("Digite um numero inteiro: "))
num_primos=[]


for i in range(2, num + 1):
    primo = True
    for x in range(2, i):
        if i % x == 0:
            primo = False
            break
    if primo:
        num_primos.append(i)

print("Os numeros primos entre 1 e ",num," é: ")
print(num_primos)

