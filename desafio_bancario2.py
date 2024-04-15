def menu():
    menu = """\n
    ================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[n] Nova Conta
[u] Cadastrar Usuário
[q] Sair
=> """
    return menu

# função depositar
def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# função sacar
def sacar(saldo, extrato, numero_saques, limite_saques, limite):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! O valor informado é maior que o saldo.")
    elif excedeu_limite:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! Verifique o valor.")
    return saldo, extrato, numero_saques

# exibir extrato
def ver_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# cadastrar usuário
def cadastrar_usuario(usuarios):
    CPF = input("Informe o CPF (somente números): ")
    
    # Validação do CPF
    if not CPF.isdigit() or len(CPF) != 11:
        print("CPF inválido. Por favor, informe um CPF válido com 11 dígitos numéricos.")
        return
    
    # Verifica se já existe um usuário com o CPF informado
    for usuario in usuarios:
        if usuario['CPF'] == CPF:
            print("Já existe usuário com esse CPF!")
            return
    
    # Cadastro do novo usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento dd-mm-aaaa: ")
    endereco = input("Informe o endereço (logradouro, nº, bairro, cidade/sigla estado): ")
    
    novo_usuario = {'CPF': CPF, 'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco}
    usuarios.append(novo_usuario)
    
    print("Usuário cadastrado com sucesso!")
    return usuarios

# criar conta    
def nova_conta(agencia, numero_conta, usuario, contas):
    CPF = input("Informe o CPF do usuário: ")
    
    # Verifica se o CPF informado pertence a um usuário cadastrado
    usuario_encontrado = False
    for user in usuario:
        if user['CPF'] == CPF:
            usuario_encontrado = True
            break
    
    if not usuario_encontrado:
        print("Usuário com o CPF informado não encontrado. Cadastre o usuário primeiro.")
        return
    
    nova_conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario, 'CPF': CPF}
    contas.append(nova_conta)
    
    print("Nova conta criada com sucesso para o usuário com CPF:", CPF)


def main():
    LIMITE_SAQUES = 3
    agencia = "0001" 
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)

        elif opcao == "e":
            ver_extrato(saldo, extrato)

        elif opcao == "u":
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "n":
            usuario=usuario
            numero_conta=contas
            nova_conta(agencia, numero_conta, usuario, contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    main()
