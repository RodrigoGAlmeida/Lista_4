#Mostre os numeros primos entre 1 e N e o numero de divisões feitas
num=int(input("Digite um numero primo: "))
num_primos=[]
divisoes=0


for i in range(2, num + 1):
    primo = True
    for x in range(2, i):
        divisoes += 1
        if i % x == 0:
            primo = False
            break
    if primo:
        num_primos.append(i)

print("Os numeros primos entre 1 e ",num," é: ")
print(num_primos)
print("divisões feitas: ", divisoes)
