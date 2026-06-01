salario=float(input("Digite o salárioa inicial: R$ "))
percentual = 0.015
for i in range (1996,2027):
       percentual *= 2
salario=salario * percentual
print(f"salário atual: R$ {salario:.2f}")
