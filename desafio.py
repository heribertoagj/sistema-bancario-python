menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""


def formataValor(valor):
    valor_formatado = "R$ "
    valor_str = str(valor).replace(".",",").split(",")
    valor_inteiro = valor_str[0]
    valor_len = len(valor_inteiro) 
    index = 0
    while True:
        if valor_len % 3 == 0 and index > 0:
            valor_formatado += "." + valor_inteiro[index]
        else:
            valor_formatado += valor_inteiro[index]

        valor_len -= 1
        index += 1
        if valor_len == 0:
            valor_formatado += ","
            break
        
    if len(valor_str[1]) > 1:
        valor_formatado += valor_str[1]        
    else:
        valor_formatado += valor_str[1] + "0"       

    return valor_formatado

def addExtrato(valor, saque):
    global extrato 

    if saque:
        extrato =  extrato + ";-" + formataValor(valor)
    else:
        extrato =  extrato + "; " + formataValor(valor)


def deposito():
    global saldo

    print("*** Depósito")
    print("")
    print("Digite valor a ser depositado")
    valor_deposito = float(input("=> "))
    if (valor_deposito < 0):
        print("Valor para depósito deve ser positivo")
    else:
        saldo += valor_deposito
        addExtrato(valor_deposito, False)
        print(f"valor depositado {formataValor(valor_deposito)} com sucesso")

def sacar():
    print("*** Sacar")
    print("")
    print("Digite valor a ser sacado")
    
    global saldo
    global numero_saques
    global LIMITE_SAQUES

    if numero_saques >= LIMITE_SAQUES:
        print(f"Numero de saques diários excedido")
        return

    valor_saque = float(input("=> "))
    if valor_saque > 500:
        print(f"Valor maximo permitido para saque é R$ 500,00")
        return
    
    if valor_saque > saldo:
        print(f"Não existe saldo disponível para este saque")
        return

    saldo -= valor_saque
    addExtrato(valor_saque, True)
    print(f"valor sacado {formataValor(valor_saque)} com sucesso")


def exibirExtrato():
    global extrato
    linha_extrato = extrato.split(";")
    tam = len(linha_extrato)
    
    print("*** Extrato")

    if tam == 0:
        print("Não existem lançamentos")
    else:
        for i in range(tam):
            print(f" {linha_extrato[i]}")
    
    print("")
    print(f"Saldo disponível => {formataValor(saldo)}")
    


while True:

    opcao = input(menu)

    if opcao == "d" :
        deposito()

    elif opcao == "s":
        sacar()

    elif opcao == "e":
        exibirExtrato()
    elif opcao == "q":
        break;
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")