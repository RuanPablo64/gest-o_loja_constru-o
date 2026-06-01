# um sistema de gestão para um loja de material de construção
# nome ficticio da loja: Cimentos Import's
#modulos: produtos, clientes, entregas
#Crud's: cadastrar, atualizar, deletar e mostrar
print()
print()
decisao = "0"
while decisao != "5":
    print(''''
  ______  __  .___  ___.  _______ .__   __. .___________.  ______        _______.
 /      ||  | |   \/   | |   ____||  \ |  | |           | /  __  \      /       |
|  ,----'|  | |  \  /  | |  |__   |   \|  | `---|  |----`|  |  |  |    |   (----`
|  |     |  | |  |\/|  | |   __|  |  . `  |     |  |     |  |  |  |     \   \    
|  `----.|  | |  |  |  | |  |____ |  |\   |     |  |     |  `--'  | .----)   |   
 \______||__| |__|  |__| |_______||__| \__|     |__|      \______/  |_______/    
                                                                                 
''')
    print()
    print()
    print()
    print('''' 
 __  .___  ___. .______     ______   .______      .___________. __      _______.
|  | |   \/   | |   _  \   /  __  \  |   _  \     |           |(_ )    /       |
|  | |  \  /  | |  |_)  | |  |  |  | |  |_)  |    `---|  |----` |/    |   (----`
|  | |  |\/|  | |   ___/  |  |  |  | |      /         |  |             \   \    
|  | |  |  |  | |  |      |  `--'  | |  |\  \----.    |  |         .----)   |   
|__| |__|  |__| | _|       \______/  | _| `._____|    |__|         |_______/    
   ''')
    print()
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
    print("#      1 - produtos         #")
    print("#      2 - Clientes         #")
    print("#      3 - Entregas         #")
    print("#      4 - Relatorios       #")
    print("#      5 - Sair do Progama  #")
    print("#                           #")
    print("#                           #")
    print("#############################")
    print("#############################")
    print()
    print()
    decisao = input("escolha uma das opções listadas: ")
    print()
    if decisao == "1":
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
        print("#      2 - Ajustar          #")
        print("#      3 - Excluir          #")
        print("#                           #")
        print("#############################")
        print("#############################")
        print()
        print()
        decisao_produtos = input("por favor, escolha uma das opções listadas: ")
        if decisao_produtos == "1":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
        elif decisao_produtos == "2":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
        elif decisao_produtos == "3":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
    elif decisao == "2":
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
        print("#      1 - Criar Conta      #")
        print("#      2 - atualizar        #")
        print("#      3 - Apagar Conta     #")
        print("#                           #")
        print("#############################")
        print("#############################")
        print()
        print()
        decisao_clientes = input("escolha uma das opções listadas: ")
        if decisao_clientes == "1":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
        elif decisao_clientes == "2":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
        elif decisao_clientes == "3":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
    elif decisao == "3":
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
        print("#    2 - Status de Entrega  #")
        print("#    3 - Cancelar Entrega   #")
        print("#                           #")
        print("#############################")
        print("#############################")
        print()
        print()
        decisao_entrega = input("escolha uma das opções listadas: ")
        if decisao_entrega == "1":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
        elif decisao_entrega == "2":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
        elif decisao_entrega == "3":
            print("perdoe-nos, mas essa função do sistema está em progesso de criação")
    elif decisao == "4":
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
print()       
print("fim do progama")
