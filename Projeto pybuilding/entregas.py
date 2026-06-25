import funcoes_gerais
from funcoes_gerais import logo
from funcoes_gerais import limpador
def modulo_entregas(entregas, clientes, produtos):
    decisao_entrega = "0"
    while decisao_entrega != "5":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+      Modulo Entregas      +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#    1 - Registar Entrega   #")
            print("#    2 - Ver Entregas       #")
            print("#    3 - Status da Entrega  #")
            print("#    4 - Cancelar Pendencia #")
            print("#    5 - Sair do Modulo     #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_entrega = input("escolha uma das opções listadas: ")
            if decisao_entrega == "1":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+     Registrar Entrega     +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                # nota importante: no registro de entrega (e também na atualização do mesmo modulo) fiz uma correlação entre o 1 e 2 modulo
                # o sistema pede para o usuario o EAN do produto e senha de um cliente cadastrado no sistema
                # caso ele não encontre o produto ou o cliente, a entrega não é registrada, e caso o produto não esteja em estoque, a entrega também não é registrada
                # ou seja, a entrega é registrada caso ambos estejam cadastrados, interligando ambos os modulos no terceiro
                rua = input("digite o nome da rua que a entrega tem que ser feita: ")
                while rua in entregas:
                    print("a rua informada para entrega já está registrada no sistema")
                    print("tente novamente")
                    rua = input("digite o nome da rua que a entrega tem que ser feita: ")
                print()
                ean_produto = input("digite o codigo do produto para a entrega: ")
                if ean_produto in produtos and produtos[ean_produto]["estoque"] == "disponivel":
                    print()
                    senha_cliente = input("digite a senha de usuario que está registrando a entrega: ")
                    if senha_cliente in clientes:
                        print()
                        data_entrega = input("digite a data que será realizada a entrega (DD/MM/AAAA): ")
                        while not funcoes_gerais.validar_data_entrega(data_entrega):
                            print("tente novamente")
                            data_entrega = input("digite a data que será realizada a entrega (DD/MM/AAAA): ")
                        pendencia = "pendente"
                        print()
                        entregas[rua] = {"produto": produtos[ean_produto]["nome"], "cliente" : clientes[senha_cliente]["nome"], "data" : data_entrega, "pendencia" : pendencia }
                        print()
                        print(entregas)
                        print()
                        print("uma nova entrega foi cadastrada no sistema!")
                        sair = input("aperte <enter> para sair do sistema: ")
                    else:
                        print("o cliente não está registrado no sistema para registrar a entrega: ")
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
            elif decisao_entrega == "2":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+   Procurar Por Entregas   +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                metodo = input("escolha a forma de procura da entrega [nome da rua(1)/nome do produto(2)/nome do cliente(3)]: ")
                if metodo == "1":
                    busca = input("digite a rua da entrega cadastrada: ")
                    if busca in entregas:
                        print(f"nome do produto a ser entregue: {entregas[busca]["produto"]}")
                        print(f"nome do cliente: {entregas[busca]["cliente"]}")
                        print(f"data de entrega: {entregas[busca]["data"]}")
                        print(f"Pendencia: {entregas[busca]["pendencia"]}")
                        print()
                        sair = input("aperte <enter> para sair: ")
                    else:
                        print("a entrega não está cadastrada no sistema")
                        sair = input("aperte <enter> para sair: ")
                elif metodo == "2":
                    print()
                    busca_produto = input("digite o nome do produto: ")
                    contador = 0
                    for rua in entregas:
                        if entregas[rua]["produto"].startswith(busca_produto):
                            print(f"rua da entrega: {rua}")
                            print(f"nome do cliente: {entregas[rua]["cliente"]}")
                            print(f"data de entrega: {entregas[rua]["data"]}")
                            print(f"Pendencia: {entregas[rua]["pendencia"]}")
                            print()
                            contador += 1
                    if contador == 0:
                        print("o produto informado não está registrado em nenhuma entrega")
                        sair = input("aperte <enter> para sair: ")
                    else:
                        sair = input("aperte <enter> para sair: ")
                elif metodo == "3":
                    print()
                    busca_cliente = input("digite o primeiro nome do cliente: ")
                    contador = 0
                    for rua in entregas:
                        if entregas[rua]["cliente"].startswith(busca_cliente):
                            print(f"rua da entrega: {rua}")
                            print(f"nome do produto: {entregas[rua]["produto"]}")
                            print(f"data de entrega: {entregas[rua]["data"]}")
                            print(f"Pendencia: {entregas[rua]["pendencia"]}")
                            print()
                            contador += 1
                    if contador == 0:
                        print("o cliente informado não está registrado em nenhuma entrega")
                        sair = input("aperte <enter> para sair: ")
                    else:
                        sair = input("aperte <enter> para sair: ")
            elif decisao_entrega == "3":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Status de Entrega    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                #aqui também se encontra a mesma ideia de que caso o cliente ou produto não esteja cadastrado, a entrega não é atualizada
                alteracao = input("digite a rua da entrega cadastrada: ")
                if alteracao in entregas:
                    print(f"nome do produto: {entregas[alteracao]["produto"]}")
                    print(f"nome do cliente: {entregas[alteracao]["cliente"]}")
                    print(f"data de entrega: {entregas[alteracao]["data"]}")
                    print(f"pendencia: {entregas[alteracao]["pendencia"]}")
                    print()
                    continuar = input("aperte <enter> para iniciar as alterações: ")
                    decisao_alteracao = "0"
                    while decisao_alteracao != "5":
                        limpador()
                        logo()
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        print("+                           +")
                        print("+       1 - Produto         +")
                        print("+       2 - Cliente         +")
                        print("+       3 - Data            +")
                        print("+       4 - Pendencia       +")
                        print("+       5 - Sair            +")
                        print("+                           +")
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        decisao_alteracao = input("escolha a opção na qual deseja alterar: ")
                        print()
                        if decisao_alteracao == "1":
                            print()
                            novo_ean_produto = input("informe o codigo do novo produto a ser entregue: ")
                            if novo_ean_produto not in produtos or produtos[novo_ean_produto]["estoque"] != "disponivel":
                                if novo_ean_produto not in produtos:
                                    print("o produto solicitado não está cadastrado no sistema")
                                    sair = input("aperte <enter> para voltar")
                                elif produtos[novo_ean_produto]["estoque"] != 2:
                                    print("o produto solicitado não está em estoque/disponivel no momento")
                                    sair = input("aperte <enter> para voltar: ")
                            else:
                                print()
                                entregas[alteracao]["produto"] = produtos[novo_ean_produto]["nome"]
                                print(entregas)
                                print()
                                print("o status da entrega foi atualizado com sucesso")
                                sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "2":
                            print()
                            nova_senha_cliente = input("digite a senha do novo cliente que solicitou a entrega: ")
                            if nova_senha_cliente not in clientes:
                                print()
                                print("a senha do cliente solicitado não está registrado no sistema")
                                sair = input("aperte <enter> para voltar: ")
                            else:
                                entregas[alteracao]["cliente"] = clientes[nova_senha_cliente]["nome"]
                                print()
                                print(entregas)
                                print()
                                print("o status da entrega foi atualizado com sucesso")
                                sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "3":
                            print()
                            data_entrega = input("digite a nova data de entrega do pedido: ")
                            while not funcoes_gerais.validar_data_entrega(data_entrega):
                                print("tente novamente")
                                data_entrega = input("digite a nova data de entrega do pedido: ")
                            print()
                            entregas[alteracao]["data"] = data_entrega
                            print(entregas)
                            print()
                            print("o status da entrega foi atualizado com sucesso")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "4":
                            print()
                            if entregas[alteracao]["pendencia"] == "pendente":
                                print("a entrega ainda está pendente. Caso queira confirmar que a entrega foi finalizada, acesse a área de cancelamente de pendencia desse modulo")
                                sair = input("aperte <enter> para voltar")
                            else:
                                mudanca = input("tem certeza de que deseja confirmar essa entrega como pendente?")
                                if mudanca.lower() == "s" or mudanca.lower() == "sim":
                                    print()
                                    entregas[alteracao]["pendencia"] == "pendente"
                                    print(entregas)
                                    print()
                                    print("o status da entrega foi atualizado com sucesso")
                                    sair = input("aperte <enter> para voltar")
                                else:
                                    print("mudança cancelada!")
                                    sair = input("aperte <enter> para voltar")
                        elif not (decisao_alteracao.isdigit()) or (decisao_alteracao <= "0" or decisao_alteracao > "5"):
                            print()
                            print("você digitou uma opção invalida. Tente digitar uma opção dentre as solicitadas")
                            sair = input("aperte <enter> para voltar: ")
            elif decisao_entrega == "4":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Cancelar Pendencia   +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                excluir = input("digite a rua da entrega que será informada como feita ")
                if excluir in entregas:
                    print()
                    print(f"nome do produto a ser entregue: {entregas[excluir]["produto"]}")
                    print(f"nome do cliente: {entregas[excluir]["cliente"]}")
                    print(f"data de entrega: {entregas[excluir]["data"]}")
                    print(f"pendencia: {entregas[excluir]["pendencia"]}")
                    print()
                    if not funcoes_gerais.validar_pendencia(excluir, entregas):
                        sair = input("aperte <enter> para sair")
                    else:
                        certeza = input("você tem certeza de que deseja atualizar a entrega como feita?: ")
                        if certeza.lower() == "s" or certeza.lower() == "sim":
                            entregas[excluir]["pendencia"] = "feita"
                            print()
                            print(entregas)
                            print()
                            print("a entrega foi realizada com sucesso!")
                            sair = input("aperte <enter> para sair: ")
                        else:
                            print("exclusão cancelada!")
                            sair = input("aperte <enter> para sair: ")
                else:
                    print("a entrega listada não está cadastrada no sistema")
                    sair = input("aperte <enter> para sair: ")
            elif not (decisao_entrega.isdigit()) or (decisao_entrega <= "0" or decisao_entrega > "5"):
                print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
                sair = input("aperte <enter> para voltar")