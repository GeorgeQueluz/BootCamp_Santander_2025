menu = """
============= MENU =============

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

================================           
=>: """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Digite o valor do Depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato+=f"Depósito: R$ {valor:.2f}\n"
                print("===== Realizado com sucesso ====")
            else:
                print("Valor incorreto, tente novamente")

        except ValueError:
            print("Valor incorreto, tente novamente")
        

    elif opcao == "s":
        try:   
            valor = float(input("Digite valor do saque: R$ "))
            if numero_saques >= LIMITE_SAQUES:
                print("Limite de saques diários atingido")

            elif valor > limite_saque:
                print("Valor máximo por saque é de R$ 500,00")
        
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("===== Realizado com sucesso ====")

        except ValueError:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "e":
        print("\n=========== Extrato ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")