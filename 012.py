#Calcular o fatorial de N numeros

num=int(input("digite o numero fatorial: "))
fatorial=1
conta=""

print("Fatorial de: ",num)
for i in range(num,0,-1):
    fatorial *= i
    if i > 1:
        conta += str(i) + ". "
    elif i == 1:
        conta += str(i)

print(f"{num}! {conta} = {fatorial}")