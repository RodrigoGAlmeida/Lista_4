#caixa registradora rudimentar
#encera ao digitar 0

repetir = True
while repetir:
    total = 0
    valor = 0
    produto = 1
  
    print("Lojas Tabajara")
    valor = int(input(f"Digite o valor do produto {produto}: "))
    while valor != 0:
        print(f"Produto {produto}: R${valor}")
        total += valor
        produto += 1
        valor = int(input(f"Digite o valor do produto {produto}: "))
    print("Total: R$", total)
    dinheiro=float(input("Digite a quantidade paga em dinheiro: "))
    troco=dinheiro-total
    print("Troco: R$",troco)
