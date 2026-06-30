import funcoes_gerais
def cadastro_produto(produtos):
    print()
    print()
    ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
    funcoes_gerais.validar_ean(ean, produtos)
    print()
    nome = input("digite o nome do produto: ")
    funcoes_gerais.validar_nome_produto(nome, produtos)
    print()
    preco = input("digite um preço para o produto: ")
    while not funcoes_gerais.validar_preco(preco):
        preco = input("digite um preço para o produto: ")
    print()
    categoria = input("digite a categoria do produto: ")
    while categoria == "":
        print("você digitou uma categoria vazia. Tente novamente")
        categoria = input("digite a categoria do produto: ")
    print()
    estoque = "disponivel"
    print()
    produtos[ean] = {"nome" : nome.lower(), "preço" : float(preco), "categoria" : categoria.lower(), "estoque" : estoque}
    print(produtos)
    print()
    print("o cadastro do produto foi bem sucedido!")
    print()
    sair = input("aperte <enter> para sair: ")


    
def cadastro_clientes(clientes):
    print()
    print()
    senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
    funcoes_gerais.validar_senha(senha, clientes)
    print()
    nome = input("digite o nome do usuario: ")
    print()
    email = input("digite o email do usuario: ")
    while not funcoes_gerais.validar_email(email):
        print("tente novamente")
        email = input("digite o email do usuario: ")
    print()
    telefone = input("digite o numero de telefone do usuario: ")
    while not funcoes_gerais.validar_telefone(telefone):
        print("tente novamente")
        telefone = input("digite o numero de telefone do usuario: ")
    print()
    aniversario = input("digite o nascimento do usuario (DD/MM/AAAA): ")
    while not funcoes_gerais.validar_tempo_aniversario(aniversario):
        print("tente novamente")
        aniversario = input("digite o nascimento do usuario (DD/MM/AAAA): ")
    print()
    status = "ativo"
    clientes[senha] = {"nome" : nome, "email" : email, "telefone" : telefone, "aniversario" : aniversario, "status" : status}
    print(clientes)
    print()
    print("bem-vindo!")
    print("um novo cliente foi cadastrado no sistema")
    print()
    sair = input("aperte <enter> para sair: ")



def cadastrar_entrega(entregas, clientes, produtos):
    print()
    endereco = input("digite o endereço do terreno para que sera entregue: ")
    while endereco in entregas:
        print("o endereço informado já está cadastrado no sistema")
        print("tente novamente")
        endereco = input("digite o endereço do terreno para que sera entregue: ")
    print()
    rua = input("dgite o nome da rua que será feita a entrega: ")
    while rua == "":
        print("você digitou uma rua vazia, tente novamente")
        rua = input("dgite o nome da rua que será feita a entrega")
    print()
    ean_produto = input("digite o codigo do produto para a entrega: ")
    if ean_produto in produtos and produtos[ean_produto]["estoque"] == "disponivel":
        print()
        senha_cliente = input("digite a senha de usuario que está registrando a entrega: ")
        if senha_cliente in clientes and clientes[senha_cliente]["status"] == "ativo":
            print()
            data_entrega = input("digite a data que será realizada a entrega (DD/MM/AAAA): ")
            while not funcoes_gerais.validar_data_entrega(data_entrega):
                print("tente novamente")
                data_entrega = input("digite a data que será realizada a entrega (DD/MM/AAAA): ")
            pendencia = "pendente"
            print()
            entregas[endereco] = {"rua" : rua, "produto" : ean_produto, "cliente" : senha_cliente, "data" : data_entrega, "pendencia" : pendencia }
            print()
            print(entregas)
            print()
            print("uma nova entrega foi cadastrada no sistema!")
            sair = input("aperte <enter> para sair do sistema: ")
        elif senha_cliente not in clientes and clientes[senha_cliente]["status"] != "ativo":
            if senha_cliente not in clientes:
                print("o cliente não está registrado no sistema para registrar a entrega: ")
                sair = input("aperte <enter> para sair do sistema: ")
            elif clientes[senha_cliente]["status"] != "ativo":
                print("o cliente informado não está mais ativo no sistema")
                sair = input("aperte <enter> para sair do sistema: ")
    elif ean_produto not in produtos or produtos[ean_produto]["estoque"] != "disponivel":
        if ean_produto not in produtos:
            print("o produto informado não está cadastrado no sistema")
            print()
            sair = input("aperte <enter> para sair do sistema: ")
        elif produtos[ean_produto]["estoque"] != "disponivel":
            print("o produto informado não está em estoque no momento")
            print()
            sair = input("aperte <enter> para sair do sistema: ")