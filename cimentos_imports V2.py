# um sistema de gestão para um loja de material de construção
# nome ficticio da loja: Cimentos Import's
#modulos: produtos, clientes, entregas
#Crud's: cadastrar, atualizar, deletar e mostrar
#atualizações: adicionei uma função para limpar o terminal e uma outra função para a logo do nome da loja aparecer em todas as ocasiões
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
    # codigo chave (EAN/codigo de barras) : nome, preço, em estoque
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
    #codigo chave(endereço) : nome do produto, nome do cliente, pendente ou não
    "rua da uf" : ["Cimento", "Ruan Pablo", "pendente" ],
    "rua do if" : ["Cal", "Julio Cesar", "pendente"],
    "rua do centro" : ["Tijolo", "Mateus Batista", "feita"]
}
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
                ean = input("digite um codigo para o produto: ")
                print()
                nome = input("digite o nome do produto: ")
                print()
                preco = input("digite um preço para o produto: ")
                print()
                estoque = input("digite se ele está em estoque/disponivel: ")
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
                    print("A seguir, digite as alterações necessarias")
                    print()
                    novo_nome = input("digite o novo nome: ")
                    print()
                    novo_preco = input("digite o novo preço: ")
                    print()
                    nova_disponibilidade = input("digite a nova disponibilidade: ")
                    produtos[alteracao] = [novo_nome, novo_preco, nova_disponibilidade]
                    print()
                    print(produtos)
                    print("a alteração foi bem sucedida!")
                    print()
                    sair = input("aperte <enter> para sair: ")
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
    elif decisao == "2":
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
            print("#     3 - Atualizar usuario #")
            print("#     4 - Apagar Conta      #")
            print("#     5 - sair do modulo    #")
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
                senha = input("digite a senha de usuario: ")
                print()
                nome = input("digite o nome do usuario: ")
                print()
                email = input("digite o email do usuario: ")
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
                    print()
                    print("A seguir, digite as alterações necessarias")
                    print()
                    novo_nome = input("digite o novo nome do usuario: ")
                    print()
                    novo_email = input("digite o novo email do usuario: ")
                    print()
                    novo_fone = input("digite o novo numero de telefone do usuario: ")
                    clientes[alteracao] = [novo_nome, novo_email, novo_fone]
                    print()
                    print(clientes)
                    print("a alteração foi bem sucedida!")
                    print()
                    sair = input("aperte <enter> para sair: ")
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
            print("#    4 - cancelar entrega   #")
            print("#                           #")
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
                alteracao = input("digite a rua da entrega cadastrada: ")
                if alteracao in entregas:
                    print(f"nome do produto: {entregas[alteracao][0]}")
                    print(f"nome do cliente: {entregas[alteracao][1]}")
                    print(f"pendencia: {entregas[alteracao][2]}")
                    print()
                    print()
                    print("A seguir, digite as alterações necessarias")
                    print()
                    novo_produto_cadastrado = input("digite a senha do novo produto para ser entregue: ")
                    if novo_produto_cadastrado in produtos and produtos[novo_produto_cadastrado][2] == "disponivel":
                        print()
                        nova_senha_cliente = input("digite a senha do novo cliente para a entrega: ")
                        if nova_senha_cliente in clientes:
                            nova_pendencia = input("digite a nova pendencia da entrega: ")
                            entregas[alteracao] = [novo_produto_cadastrado, nova_senha_cliente, nova_pendencia]
                            print()
                            print(entregas)
                            print()
                            print("o status da entrega foi atualizada com sucesso: ")
                            sair = input("aperte <enter> para sair: ")
                        else:
                            print("O cliente com status para ser alterado não está cadastrado no sistema")
                            print()
                            sair = input("aperte <enter> para sair: ")
                    else:
                        print("o novo produto a ser entregue não está cadastrado no sistema ou não está disponivel")
                        print()
                        sair = input("aperte <enter> para sair: ")
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
            print("#    4 - sair do modulo     #")
            print("#                           #")
            print("#############################")
            print("#############################")
            print()
            print()
            decisao_relatorios = input("escolha uma das opções listadas: ")
            if decisao_relatorios == "1":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
            elif decisao_relatorios == "2":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
            elif decisao_relatorios == "3":
                print("perdoe-nos, mas essa função do sistema está em progesso de criação")
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
