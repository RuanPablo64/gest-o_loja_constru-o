import pickle
import os 
# um sistema de gestão para um loja de material de construção
# nome ficticio da loja: Cimentos Import's
#modulos: produtos, clientes, entregas
#Crud's: cadastrar, mostrar, atualizar e deletar
#atualizações: adicionei uma função para limpar o terminal (para não necessitar do uso de bibliotecas) e uma outra função para a logo do nome da loja aparecer em todas as ocasiões
#observação: estou focando em fazer o codigo funcional para na versão final polir o mesmo e deixar sua interface mais bonita
def limpador():
    print("\033[H\033[J", end="")
def logo():
        print('''
                                                                                                                       
   mmm  mmmmm  m    m mmmmmm mm   mmmmmmmm  mmmm   mmmm         mmmmm  m    m mmmmm   mmmm  mmmmm mmmmmmm   m          
 m"   "   #    ##  ## #      #"m  #   #    m"  "m #"   "          #    ##  ## #   "# m"  "m #   "#   #      #     mmm  
 #        #    # ## # #mmmmm # #m #   #    #    # "#mmm           #    # ## # #mmm#" #    # #mmmm"   #           #   " 
 #        #    # "" # #      #  # #   #    #    #     "#          #    # "" # #      #    # #   "m   #            """m 
  "mmm" mm#mm  #    # #mmmmm #   ##   #     #mm#  "mmm#"        mm#mm  #    # #       #mm#  #    "   #           "mmm" 
                                                                                                                       
                                                                                                                                    
    ''')
#

produtos = {
    # codigo chave (EAN/codigo de barras) : nome, preço, em estoque (obs: a disponibilidade/ estoque do produto será importante para o modulo entregas)
    "11111111" : ["Cimento", "3,5","disponivel"],
    "22222222" : ["Cal", "1,5", "disponivel"],
    "33333333" : ["Tijolo", "1,0", "disponivel"]
}
clientes = {
    #codigo chave(senha de acesso) : nome, email, telefone
    "64646464" : ["Ruan Pablo", "RuanP@gmail.com", "9966-0000"],
    "45454545" : ["Julio cesar", "JulioXD@gmail.com", "9813-0001"],
    "12121212" : ["Mateus Batista", "MTB@gmail.com", "9121-0002"]
}
entregas = {
    #codigo chave(endereço) : nome do produto para ser entregue, nome do cliente que registrou a entrega, entrega pendente ou feita
    "rua da uf" : ["Cimento", "Ruan Pablo", "pendente" ],
    "rua do if" : ["Cal", "Julio Cesar", "pendente"],
    "rua do centro" : ["Tijolo", "Mateus Batista", "feita"]
}
#importei a biblioteca Os para verificar a existencia dos arquivos criados, e caso existam, ele realiza a leitura em binario
#caso não exista, ele passa direto. entretanto, no final do codigo existe a gravação do arquivo, que guarda todas as informações dos dicionarios acima
#Claro, se durante o codigo, o gestor tiver adicionado, atualizado ou excluido informações, elas vão ser salvas e gravadas no final
if os.path.exists("produtos.dat"):
    arqprodutos = open("produtos.dat", "rb")
    produtos = pickle.load(arqprodutos)
    arqprodutos.close()
if os.path.exists("clientes.dat"):
    arqclientes = open("clientes.dat", "rb")
    clientes = pickle.load(arqclientes)
    arqclientes.close()
if os.path.exists("entregas.dat"):
    arqentregas = open("entregas.dat", "rb")
    entregas = pickle.load(arqentregas)
    arqentregas.close()

decisao = "0"
while decisao != "6":
    limpador()
    logo()
    print()
    print()
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+                           +")
    print("+        BEM - VINDO        +")
    print("+                           +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("#############################")
    print("#                           #")
    print("#                           #")
    print("#      1 - Produtos         #")
    print("#      2 - Clientes         #")
    print("#      3 - Entregas         #")
    print("#      4 - Relatorios       #")
    print("#      5 - Sobre o Sistema  #")
    print("#      6 - Sair do Progama  #")
    print("#                           #")
    print("#                           #")
    print("#                           #")
    print("#############################")
    print("#############################")
    print()
    print()
    decisao = input("escolha uma das opções listadas: ")
    print()
    if decisao == "1":
        decisao_produtos = "0"
        while decisao_produtos != "5":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+      Modulo Produtos      +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#      1 - Cadastrar        #")
            print("#      2 - Visualizar       #")
            print("#      3 - Ajustar          #")
            print("#      4 - Excluir          #")
            print("#      5 - Sair do Modulo   #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_produtos = input("por favor, escolha uma das opções listadas: ")
            if decisao_produtos == "1":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Cadastrar produto    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                print()
                ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
                while ean in produtos:
                    print("o codigo do produto registrado já está cadastrado no sistema")
                    print("Tente novamente")
                    print()
                    ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
                while (not(ean.isdigit())) or (len(ean) != 8):
                    if not ean.isdigit():
                        print()
                        print("o codigo precisa possuir apenas numeros. Tente Novamente")
                        ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
                    elif len(ean) != 8:
                        print()
                        print("o codigo precisa ter exatamente 8 digitos. Tente Novamente")
                        ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
                else:
                    print()
                    nome = input("digite o nome do produto: ")
                    print()
                    preco = input("digite um preço para o produto: ")
                    print()
                    estoque = input("digite se ele está disponivel: ")
                    while estoque != "disponivel" and estoque != "Insdisponivel":
                        print()
                        print("por favor, digite se ele está 'disponivel' ou 'indisponivel', apenas")
                        print("tente novamente")
                        estoque = input("digite se ele está disponivel: ")
                    print()
                    produtos[ean] = [nome, preco, estoque]
                    print(produtos)
                    print()
                    print("o cadastro do produto foi bem sucedido!")
                    print()
                    sair = input("aperte <enter> para sair: ")
            elif decisao_produtos == "2":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Procurar produtos    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                busca = input("digite o codigo do produto que você deseja visualizar: ")
                if busca in produtos:
                    print(f"nome do produto: {produtos[busca][0]}")
                    print(f"preço do produto: {produtos[busca][1]}")
                    print(f"disponibilidade do produto: {produtos[busca][2]}")
                    print()
                    sair = input("aperte <enter> para sair: ")
                else:
                    print("o codigo do produto não está registrado no sistema")
                    sair = input("aperte <enter> para sair: ")
            elif decisao_produtos == "3":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Alterar produtos     +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                alteracao = input("digite o codigo do produto que deseja alterar: ")
                if alteracao in produtos:
                    print(f"nome do produto: {produtos[alteracao][0]}")
                    print(f"preço do produto: {produtos[alteracao][1]}")
                    print(f"disponibilidade do produto: {produtos[alteracao][2]}")
                    print()
                    continuar = input("aperte <enter> para iniciar as alterações: ")
                    decisao_alteracao = "0"
                    while decisao_alteracao != "4":
                        limpador()
                        logo()
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        print("+                           +")
                        print("+       1 - Nome            +")
                        print("+       2 - Preço           +")
                        print("+       3 - Estoque         +")
                        print("+       4 - Sair            +")
                        print("+                           +")
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        decisao_alteracao = input("escolha a opção na qual deseja alterar: ")
                        print()
                        if decisao_alteracao == "1":
                            limpador()
                            logo()
                            print()
                            novo_nome = input("digite o novo nome do produto: ")
                            print()
                            produtos[alteracao][0] = novo_nome
                            print()
                            print(produtos)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar: ")
                        elif decisao_alteracao == "2":
                            limpador()
                            logo()
                            print()
                            novo_preco = input("digite o novo preço do produto: ")
                            print()
                            produtos[alteracao][1] = novo_preco
                            print()
                            print(produtos)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar: ")
                        elif decisao_alteracao == "2":
                            limpador()
                            logo()
                            print()
                            novo_preco = input("digite o novo preço do produto: ")
                            print()
                            produtos[alteracao][1] = novo_preco
                            print()
                            print(produtos)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar: ")
                        elif decisao_alteracao == "3":
                            limpador()
                            logo()
                            print()
                            nova_disponibilidade = input("digite a nova disponibilidade do produto: ")
                            while nova_disponibilidade != "disponivel" and nova_disponibilidade != "indisponivel":
                                print()
                                print("por favor, digite se ele está 'disponivel' ou 'indisponivel', apenas")
                                print("tente novamente")
                                nova_disponibilidade = input("digite a nova disponibilidade: ")
                            print()
                            produtos[alteracao][2] = nova_disponibilidade
                            print()
                            print(produtos)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar: ")
                        elif not (decisao_alteracao.isdigit()) or (decisao_alteracao <= "0" or decisao_alteracao > "4"):
                            print()
                            print("você digitou uma opção invalida. Tente digitar uma opção dentre as solicitadas")
                            sair = input("aperte <enter> para voltar: ")
                else:
                    print("o produto que você quer alterar não está cadastrado no sistema")
                    print()
                    sair = input("aperte <enter> para sair: ")
            elif decisao_produtos == "4":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+    exclusão de produtos   +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                excluir = input("digite o codigo do produto que deseja excluir: ")
                if excluir in produtos:
                    print()
                    print(f"nome do produto: {produtos[excluir][0]}")
                    print(f"preço do produto: {produtos[excluir][1]}")
                    print(f"disponibilidade do produto: {produtos[excluir][2]}")
                    print()
                    certeza = input("você tem certeza de que deseja excluir esse produto?: ")
                    #o lower() serve para deixar letras maiusculas em minusculas, caso o usuario as digite em maiusculas
                    if certeza.lower() == "s" or certeza.lower() == "sim":
                        del produtos[excluir]
                        print()
                        print(produtos)
                        print()
                        print("o produto foi excluido com sucesso!")
                        sair = input("aperte <enter> para sair: ")
                    else:
                        print("exclusão cancelada!")
                        sair = input("aperte <enter> para sair: ")
                else:
                    print("o codigo do produto não está cadastrado no sistema")
                    sair = input("aperte <enter> para sair: ")
            elif not (decisao_produtos.isdigit()) or (decisao_produtos <= "0" or decisao_produtos > "5"):
                print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
                sair = input("aperte <enter> para voltar")
        decisao_clientes = "0"
        while decisao_clientes != "5":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+      Modulo Clientes      +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#     1 - Criar Conta       #")
            print("#     2 - Ver Clientes      #")
            print("#     3 - Atualizar Usuario #")
            print("#     4 - Apagar Conta      #")
            print("#     5 - Sair do Modulo    #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_clientes = input("escolha uma das opções listadas: ")
            if decisao_clientes == "1":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Criação de Conta     +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                print()
                senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
                while senha in clientes:
                    print("a senha do cliente solicitado já está cadastrada no sistema")
                    print("tente novamente")
                    print()
                    senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
                while (not(senha.isdigit())) or (len(senha) != 8):
                    if not senha.isdigit():
                        print()
                        print("a senha de usuario precisa possuir apenas numeros. Tente Novamente")
                        senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
                    elif len(senha) != 8:
                        print()
                        print("a senha precisa ter exatamente 8 digitos. Tente Novamente")
                        senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ") 
                print()
                nome = input("digite o nome do usuario: ")
                print()
                email = input("digite o email do usuario: ")
                print()
                telefone = input("digite o numero de telefone do usuario: ")
                while len(telefone) != 9:
                    print("o numero de telefone deve possuir 9 digitos. tente novamente")
                    print()
                    telefone = input("digite o numero de telefone do usuario: ")
                print()
                clientes[senha] = [nome, email, telefone]
                print(clientes)
                print()
                print("bem-vindo!")
                print("um novo cliente foi cadastrado no sistema")
                print()
                sair = input("aperte <enter> para sair: ")
            elif decisao_clientes == "2":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Procurar Clientes    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                busca = input("digite a senha do usuario para busca: ")
                if busca in clientes:
                    print(f"nome do cliente: {clientes[busca][0]}")
                    print(f"email do cliente: {clientes[busca][1]}")
                    print(f"telefone do cliente: {clientes[busca][2]}")
                    print()
                    sair = input("aperte <enter> para sair: ")
                else:
                    print("o cliente não está cadastrado no sistema")
                    sair = input("aperte <enter> para sair: ")
            elif decisao_clientes == "3":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Atualização de       +")
                print("+          Usuario          +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                alteracao = input("digite a senha do usuario para atualização: ")
                if alteracao in clientes:
                    print(f"nome do cliente: {clientes[alteracao][0]}")
                    print(f"email do cliente: {clientes[alteracao][1]}")
                    print(f"telefone do cliente: {clientes[alteracao][2]}")
                    print()
                    continuar = input("aperte <enter> para iniciar as alterações: ")
                    decisao_alteracao = "0"
                    while decisao_alteracao != "4":
                        limpador()
                        logo()
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        print("+                           +")
                        print("+       1 - Nome            +")
                        print("+       2 - Email           +")
                        print("+       3 - Telefone        +")
                        print("+       4 - Sair            +")
                        print("+                           +")
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        decisao_alteracao = input("escolha a opção na qual deseja alterar: ")
                        print()
                        if decisao_alteracao == "1":
                            limpador()
                            logo()
                            novo_nome = input("digite o novo nome do cliente: ")
                            print()
                            clientes[alteracao][0] = novo_nome
                            print(clientes)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "2":
                            limpador()
                            logo()
                            print()
                            novo_email = input("digite o novo email do usuario: ")
                            print()
                            clientes[alteracao][1] = novo_email
                            print()
                            print(clientes)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "3":
                            limpador()
                            logo()
                            print()
                            novo_fone = input("digite no novo telefone do usuario: ")
                            while len(novo_fone) != 9:
                                print("o numero de telefone do cliente deve ter 9 digitos. tente novamente")
                                print()
                                novo_fone = input("digite no novo telefone do usuario: ")
                            print()
                            clientes[alteracao][2] = novo_fone
                            print()
                            print(clientes)
                            print()
                            print("a alteração foi bem sucedida")
                            sair = input("aperte <enter> para voltar")
                        elif not (decisao_alteracao.isdigit()) or (decisao_alteracao <= "0" or decisao_alteracao > "4"):
                            print()
                            print("você digitou uma opção invalida. Tente digitar uma opção dentre as solicitadas")
                            sair = input("aperte <enter> para voltar: ")
                else:
                    print("O cliente com status para ser alterado não está cadastrado no sistema")
                    print()
                    sair = input("aperte <enter> para sair: ")
            elif decisao_clientes == "4":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Exclusão de Conta    +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                excluir = input("digite a senha de usuario para ser excluido: ")
                if excluir in clientes:
                    print()
                    print(f"nome do cliente: {clientes[excluir][0]}")
                    print(f"email do cliente: {clientes[excluir][1]}")
                    print(f"telefone do cliente: {clientes[excluir][2]}")
                    print()
                    certeza = input("você tem certeza de que deseja excluir esse cliente do sistema?: ")
                    if certeza.lower() == "s" or certeza.lower() == "sim":
                        del clientes[excluir]
                        print()
                        print(clientes)
                        print()
                        print("o cliente foi apagado do sistema com sucesso")
                        sair = input("aperte <enter> para sair: ")
                    else:
                        print("exclusão cancelada!")
                        sair = input("aperte <enter> para sair: ")
                else:
                    print("o cliente listado não possui cadastro no sistema")
                    sair = input("aperte <enter> para sair: ")
            elif not (decisao_clientes.isdigit()) or (decisao_clientes <= "0" or decisao_clientes > "5"):
                print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
                sair = input("aperte <enter> para voltar")
    elif decisao == "3":
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
            print("#    2 - Ver entregas       #")
            print("#    3 - Status da Entrega  #")
            print("#    4 - Cancelar entrega   #")
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
                if ean_produto in produtos and produtos[ean_produto][2] == "disponivel":
                    print()
                    senha_cliente = input("digite a senha de usuario que está registrando a entrega: ")
                    if senha_cliente in clientes:
                        print()
                        pendencia = input("digite se a entrega foi feita ou está pendente: ")
                        print()
                        entregas[rua] = [produtos[ean_produto][0], clientes[senha_cliente][0], pendencia]
                        print()
                        print(entregas)
                        print()
                        print("uma nova entrega foi cadastrada no sistema!")
                        sair = input("aperte <enter> para sair do sistema: ")
                    else:
                        print("o cliente não está registrado no sistema para registrar a entrega: ")
                        sair = input("aperte <enter> para sair do sistema: ")
                elif ean_produto not in produtos or produtos[ean_produto][2] != "disponivel":
                    if ean_produto not in produtos:
                        print("o produto informado não está cadastrado no sistema")
                        print()
                        sair = input("aperte <enter> para sair do sistema: ")
                    elif produtos[ean_produto][2] != "disponivel":
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
                busca = input("digite a rua da entrega cadastrada: ")
                if busca in entregas:
                    print(f"nome do produto a ser entregue: {entregas[busca][0]}")
                    print(f"nome do cliente: {entregas[busca][1]}")
                    print(f"Pendencia: {entregas[busca][2]}")
                    print()
                    sair = input("aperte <enter> para sair: ")
                else:
                    print("a entrega não está cadastrada no sistema")
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
                    print(f"nome do produto: {entregas[alteracao][0]}")
                    print(f"nome do cliente: {entregas[alteracao][1]}")
                    print(f"pendencia: {entregas[alteracao][2]}")
                    print()
                    continuar = input("aperte <enter> para iniciar as alterações: ")
                    decisao_alteracao = "0"
                    while decisao_alteracao != "4":
                        limpador()
                        logo()
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        print("+                           +")
                        print("+       1 - Produto         +")
                        print("+       2 - Cliente         +")
                        print("+       3 - Pendencia       +")
                        print("+       4 - Sair            +")
                        print("+                           +")
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        decisao_alteracao = input("escolha a opção na qual deseja alterar: ")
                        print()
                        if decisao_alteracao == "1":
                            print()
                            novo_ean_produto = input("informe o codigo do novo produto a ser entregue: ")
                            if novo_ean_produto not in produtos or produtos[novo_ean_produto][2] != "disponivel":
                                if novo_ean_produto not in produtos:
                                    print("o produto solicitado não está cadastrado no sistema")
                                    sair = input("aperte <enter> para voltar")
                                elif produtos[novo_ean_produto][2] != 2:
                                    print("o produto solicitado não está em estoque/disponivel no momento")
                                    sair = input("aperte <enter> para voltar: ")
                            else:
                                print()
                                entregas[alteracao][0] = produtos[novo_ean_produto][0]
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
                                entregas[alteracao][1] = clientes[nova_senha_cliente][0]
                                print()
                                print(entregas)
                                print()
                                print("o status da entrega foi atualizado com sucesso")
                                sair = input("aperte <enter> para voltar")
                        elif decisao_alteracao == "3":
                            print()
                            nova_pendencia = input("digite a pendencia da entrega (pendente ou feita): ")
                            print()
                            entregas[alteracao][2] = nova_pendencia
                            print(entregas)
                            print()
                            print("o status da entrega foi atualizada com sucesso")
                            sair = input("aperte <enter> para voltar: ")
                        elif not (decisao_alteracao.isdigit()) or (decisao_alteracao <= "0" or decisao_alteracao > "4"):
                            print()
                            print("você digitou uma opção invalida. Tente digitar uma opção dentre as solicitadas")
                            sair = input("aperte <enter> para voltar: ")
            elif decisao_entrega == "4":
                limpador()
                logo()
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("+                           +")
                print("+      Cancelar Entrega     +")
                print("+                           +")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print()
                excluir = input("digite a rua da entrega que será cancelada ")
                if excluir in entregas:
                    print()
                    print(f"nome do produto a ser entregue: {entregas[excluir][0]}")
                    print(f"nome do cliente: {entregas[excluir][1]}")
                    print(f"pendencia: {entregas[excluir][2]}")
                    print()
                    certeza = input("você tem certeza de que deseja cancelar essa entrega?: ")
                    if certeza.lower() == "s" or certeza.lower() == "sim":
                        del entregas[excluir]
                        print()
                        print(entregas)
                        print()
                        print("a entrega foi cancelada com sucesso!")
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
    elif decisao == "4":
        decisao_relatorios = "0"
        while decisao_relatorios != "4":
            limpador()
            logo()
            print()
            print()
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+                           +")
            print("+     Relatorios da Loja    +")
            print("+                           +")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("#############################")
            print("#                           #")
            print("#                           #")
            print("#    1 - Sobre os Produtos  #")
            print("#    2 - Sobre os Clientes  #")
            print("#    3 - Sobre as Entregas  #")
            print("#    4 - Sair do modulo     #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_relatorios = input("escolha uma das opções listadas: ")
            if decisao_relatorios == "1":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
                sair = input("aperte <enter> para voltar")
            elif decisao_relatorios == "2":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
                sair = input("aperte <enter> para voltar")
            elif decisao_relatorios == "3":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
                sair = input("aperte <enter> para voltar")
    elif decisao == "5":
        limpador()
        logo()
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("+                           +")
        print("+      Sobre o Sistema      +")
        print("+                           +")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("#############################")
        print("#                           #")
        print("#   sistema de gestão de    #")
        print("#       uma loja de         #")
        print("#   material de construção  #")
        print("#                           #")
        print("#      Desenvolvedor:       #")
        print("#        Ruan Pablo         #")
        print("#############################")
        print("#############################")
        print()
        print()
        sair = input("aperte <enter> para sair: ")
    elif not (decisao.isdigit()) or (decisao <= "0" or decisao > "6"):
        print("você digitou uma opção invalida, tente digitar uma das opções solicitadas")
        sair = input("aperte <enter> para voltar")
    
limpador()
print()    
print()
print()
print(''''                                                                                                                         
 mm    mm    mmmm    mm        mmmmmmmm  mmmmmmmm              mmmm    mmmmmmmm  mmm  mmm  mmmmmm    mmmmmm    mmmmmmmm 
 "##  ##"   ##""##   ##        """##"""  ##""""""            m#""""#   ##""""""  ###  ###  ##""""#m  ##""""##  ##"""""" 
  ##  ##   ##    ##  ##           ##     ##                  ##m       ##        ########  ##    ##  ##    ##  ##       
  ##  ##   ##    ##  ##           ##     #######              "####m   #######   ## ## ##  ######"   #######   #######  
   ####    ##    ##  ##           ##     ##                       "##  ##        ## "" ##  ##        ##  "##m  ##       
   ####     ##mm##   ##mmmmmm     ##     ##mmmmmm            #mmmmm#"  ##mmmmmm  ##    ##  ##        ##    ##  ##mmmmmm 
   """"      """"    """"""""     ""     """"""""             """""    """"""""  ""    ""  ""        ""    """ """""""" 
                                                                                                                        
                                                                                                                        ''')   
print()
print()
print("fim do progama")

#
arqprodutos = open("produtos.dat", "wb")
pickle.dump(produtos, arqprodutos)
arqprodutos.close()

arqclientes = open("clientes.dat", "wb")
pickle.dump(clientes, arqclientes)
arqclientes.close()

arqentregas = open("entregas.dat", "wb")
pickle.dump(entregas, arqentregas)
arqentregas.close()