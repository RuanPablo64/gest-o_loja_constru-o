def procurar_produto(produtos):
    print()
    metodo = input("de qual forma deseja procurar o produtos [codigo ean(1)/nome do produto(2)]: ")
    if metodo == "1":
        busca = input("digite o codigo do produto que você deseja visualizar: ")
        if busca in produtos:
            print(f"nome do produto: {produtos[busca]["nome"]}")
            print(f"preço do produto: {produtos[busca]["preço"]}")
            print(f"categoria do produto: {produtos[busca]["categoria"]}")
            print(f"disponibilidade do produto: {produtos[busca]["estoque"]}")
            print()
            sair = input("aperte <enter> para sair: ")
        else:
            print("o codigo do produto não está registrado no sistema")
            sair = input("aperte <enter> para sair: ")
    elif metodo == "2":
        busca_nome = input("digite o nome do produto que você deseja visualizar: ")
        contador = 0
        for ean in produtos:
            if produtos[ean]["nome"].startswith(busca_nome):
                print(f"codigo ean do produto: {ean}")
                print(f"preço do produto: {produtos[ean]["preço"]}")
                print(f"categoria do produto: {produtos[ean]["categoria"]}")
                print(f"disponibilidade do produto: {produtos[ean]["estoque"]}")
                contador += 1
        if contador == 0:
            print("o produto informado com esse nome não está cadastrado no sistema")
            sair = input("aperte <enter> para sair")
        else:
            sair = input("aperte <enter> para sair")
    else:
        print("você digitou uma opção invalida")
        sair = input("aperte <enter> para sair")



def procurar_clientes(clientes):
    metodo = input("digite a maneira na qual deseja pesquisar o cliente [senha(1)/nome(2)]: ")
    if metodo == "1":
        busca = input("digite a senha do usuario para busca: ")
        if busca in clientes:
            print(f"nome do cliente: {clientes[busca]["nome"]}")
            print(f"email do cliente: {clientes[busca]["email"]}")
            print(f"telefone do cliente: {clientes[busca]["telefone"]}")
            print(f"aniversario do cliente: {clientes[busca]["aniversario"]}")
            print(f"status do cliente: {clientes[busca]["status"]}")
            print()
            sair = input("aperte <enter> para sair: ")
        else:
            print("o cliente não está cadastrado no sistema")
            sair = input("aperte <enter> para sair: ")
    elif metodo == "2":
        busca_nome = input("digite o primeiro nome do cliente que deseja procurar: ")
        contador = 0
        for senha in clientes:
            if clientes[senha]["nome"].startswith(busca_nome):
                print(f"senha do cliente: {senha}")
                print(f"email do cliente: {clientes[senha]["email"]}")
                print(f"telefone do cliente: {clientes[senha]["telefone"]}")
                print(f"aniversario do cliente: {clientes[senha]["aniversario"]}")
                print(f"status do cliente: {clientes[senha]["status"]}")
                print()
                contador += 1
        if contador == 0:
            print("o nome do cliente informado não está cadastrado no sistema")
            sair = input("aperte <enter> para sair")
        else:
            sair = input("aperte <enter> para sair")
    else:
        print("você digitou uma opção invalida")
        sair = input("aperte <enter> para sair")



def procurar_entregas(entregas):
    metodo = input("escolha a forma de procura da entrega [endereço(1)/codigo do produto(2)/senha do cliente(3)]: ")
    if metodo == "1":
        busca = input("digite o endereço da entrega: ")
        if busca in entregas:
            print(f"rua onde ocorrerá a entrega: {entregas[busca]["rua"]}")
            print(f"codigo do produto a ser entregue: {entregas[busca]["produto"]}")
            print(f"senha do cliente: {entregas[busca]["cliente"]}")
            print(f"data de entrega: {entregas[busca]["data"]}")
            print(f"Pendencia: {entregas[busca]["pendencia"]}")
            print()
            sair = input("aperte <enter> para sair: ")
        else:
            print("a entrega não está cadastrada no sistema")
            sair = input("aperte <enter> para sair: ")
    elif metodo == "2":
        print()
        busca_produto = input("digite o codigo do produto: ")
        contador = 0
        for endereco in entregas:
            if entregas[endereco]["produto"] == busca_produto:
                print(f"endereço da entrega: {endereco}")
                print(f"rua da entrega: {entregas[endereco]["rua"]}")
                print(f"senha do cliente: {entregas[endereco]["cliente"]}")
                print(f"data de entrega: {entregas[endereco]["data"]}")
                print(f"Pendencia: {entregas[endereco]["pendencia"]}")
                print()
                contador += 1
        if contador == 0:
            print("o produto informado não está registrado em nenhuma entrega")
            sair = input("aperte <enter> para sair: ")
        else:
            sair = input("aperte <enter> para sair: ")
    elif metodo == "3":
        print()
        busca_cliente = input("digite a senha do cliente: ")
        contador = 0
        for endereco in entregas:
            if entregas[endereco]["cliente"] == busca_cliente:
                print(f"endereço da entrega: {endereco}")
                print(f"rua da entrega: {entregas[endereco]["rua"]}")
                print(f"nome do produto: {entregas[endereco]["produto"]}")
                print(f"data de entrega: {entregas[endereco]["data"]}")
                print(f"Pendencia: {entregas[endereco]["pendencia"]}")
                print()
                contador += 1
        if contador == 0:
            print("o cliente informado não está registrado em nenhuma entrega")
            sair = input("aperte <enter> para sair: ")
        else:
            sair = input("aperte <enter> para sair: ")