menu = """
Selecione a opção desejada:

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

"""
saldo = 1000
saldo = float(saldo)
limite_diario_01 = 500
limite_diario = 500
saldo_limite_diario = 500
extrato = ""
quantidade_saques = 0

while True :

    opcao = input (menu)
    # Depósito
    if opcao == "d" :
        valor_deposito = float(input("Insira o valor a ser depositado: "))

        if valor_deposito > 0.0 :
            saldo += valor_deposito
            extrato += f"(+) Depósito de R${valor_deposito:.2f}\n"
            print("Valor Depositado com Sucesso.")
            
        else :
            print("Esse não é um valor válido para depósito")
    #saques      
    elif opcao == "s":
            if quantidade_saques > 2 :
                print("Saque não realizado, excedeu o limite diário de saques.")
            else :
                valor_saque = float(input("Insira o valor desejado para saque: "))
                if valor_saque > 0 :
                    if valor_saque > limite_diario_01 :
                        print(f"""  O seu limite diário para saque é de R${limite_diario_01}
                        Você já usou R${500 - limite_diario}.
                        Insira um valor igual ou abaixo de R${saldo_limite_diario} para realizar novo saque.
                        """)
                    elif valor_saque > saldo :
                        print(f"""Saldo Insuficiente. 
                        O seu saldo é de R${saldo}.
                        Insira um valor igual ou abaixo deste valor.
                        """)
                    else :
                        limite_diario -= valor_saque
                        saldo_limite_diario = limite_diario_01 - valor_saque
                        quantidade_saques += 1
                        saldo -= valor_saque
                        extrato += f"(-) Saque de R${valor_saque:.2f}\n"
                        print("Saque realizado com sucesso.")
                else:
                    print("Insira um valor válido para o saque.")
    #extrato
    elif opcao == "e":
        print("Extrato Bancário")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(extrato)
        print(f"O seu saldo atual é de R${saldo:.2f}")
    #saída
    elif opcao == "q" :
        print("Obrigado por utilizar nosso sistema. Volte Sempre.")
        break
    #opção inválida
    else :
        print("Digite uma opção válida.")


