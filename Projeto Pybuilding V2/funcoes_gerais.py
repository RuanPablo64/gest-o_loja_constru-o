from datetime import datetime
def validar_tempo_aniversario(aniversario):
    hoje = datetime.today().date()
    limite = hoje.year - 110
    try:
       nascimento = datetime.strptime(aniversario, "%d/%m/%Y").date()
       if nascimento > hoje:
           print("você digitou uma data alêm do tempo atual")
           return False
       elif nascimento.year < limite:
           print("você digitou uma data muito antiga")
           return False
       else:
           return True    
    except:
        print("você digitou uma data inexistente/invalida")
        return False
    


def validar_telefone(telefone):
    try:
        fone = telefone.split("-")
        if (len(fone[0]) + len(fone[1])) != 8 and (len(fone[0]) + len(fone[1])) != 9:
            print("você digitou um numero invalido. o numero de telefone precisa de 8 a 9 digitos.")
            return False
        elif not (fone[0].isdigit()) or not (fone[1].isdigit()):
            print("o numero de telefone só pode ter digitos. apenas")
            return False
        elif telefone == '':
            print("você digitou um numero vazio")
            return False
        else:
            return True
    except:
        if not (telefone.isdigit()):
            print("o numero de telefone só pode ter digitos. apenas")
            return False
        elif telefone != 9 or telefone != 8:
            print("você digitou um numero invalido. o numero de telefone precisa de 8 a 9 digitos.")
        elif telefone == "":
            print("você digitou um numero vazio")
            return False
        else:
            return True
        


def validar_email(email):
    gmail = "@gmail.com"
    if gmail not in email:
        print("você digitou um email invalido que não possui @gmail.com")
        return False
    elif email == '':
        print("você digitou um email vazio")
        return False
    elif not (email.endswith(gmail)):
        print("o @gmail.com precisa estar no final")
        return False
    elif len(email) == 10 or len(email) == 11:
        print("você digitou apenas o @gmail.com")
        return False
    else:
        return True
    


def validar_senha(senha, clientes):
    while senha in clientes:
        print("a senha do cliente solicitado já está cadastrada no sistema")
        print("tente novamente")
        print()
        senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
    while (not(senha.isdigit())) or (len(senha) != 8) or senha == "":
        if not senha.isdigit():
            print()
            print("a senha de usuario precisa possuir apenas numeros. Tente Novamente")
            senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
        elif len(senha) != 8:
            print()
            print("a senha precisa ter exatamente 8 digitos. Tente Novamente")
            senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")
        elif senha == '':
            print("você digitou uma senha vazia")
            senha = input("digite a senha de usuario (a senha precisa de 8 digitos): ")



def validar_ean(ean, produtos):
    while ean in produtos:
        print("o codigo do produto registrado já está cadastrado no sistema")
        print("Tente novamente")
        print()
        ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
    while (not(ean.isdigit())) or (len(ean) != 8) or ean == "":
        if not ean.isdigit():
            print()
            print("o codigo precisa possuir apenas numeros. Tente Novamente")
            ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
        elif len(ean) != 8:
            print()
            print("o codigo precisa ter exatamente 8 digitos. Tente Novamente")
            ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")
        elif ean == '':
            print("você digitou um codigo vazio")
            ean = input("digite um codigo para o produto (o codigo precisa de 8 digitos): ")



def validar_preco(preco):
    try:
        preco_real = preco.split(".")
        if preco_real[0].isdigit() and preco_real[1].isdigit():
            return True
        elif not (preco_real[0].isdigit()) or not (preco_real[1].isdigit()):
            print("o preço precia apenas de numeros, exclusivamente")
            return False
        elif preco == "":
            print("você digitou um preço vazio. tente novamente")
        elif float(preco) < 0 :
            print("você digitou um preço negativo. Tente novamente")
            return False
    except:
        if preco == "":
            print("você digitou um preço vazio. Tente novamente")
        elif float(preco) < 0:
            print("você digitou um preço vazio. Tente novamente")
        else:
            return True



def validar_data_entrega(data_entrega):
    hoje = datetime.today().date()
    limite = hoje.year + 2
    try:
        data = datetime.strptime(data_entrega, "%d/%m/%Y").date()
        if data < hoje:
            print("você digitou uma data no passado")
            return False
        elif data.year > limite:
            print("você digitou uma data muito no futuro")
            return False
        else:
            return True
    except:
        print("você digitou uma data inexistente/invalida")
        return False
    


def validar_pendencia(excluir, entregas):
    hoje = datetime.today().date()
    validacao = datetime.strptime(entregas[excluir]["data"], "%d/%m/%Y").date()
    if not hoje >= validacao:
        print("você não pode confirmar uma entrega feita sem estar no dia do prazo ou a mais. Caso a entrega tenha sido adiantada, informe na área de atualização desse modulo")
        return False
    elif entregas[excluir]["pendencia"] == "feita":
        print("a entrega já foi registrada como feita. Caso queira confirma-la como pendente, acesse a área de atualizações desse modulo")
        return False
    else:
        return True
    


def validar_nome_produto(nome, produtos):
    contador = 0
    while nome == "":
        print("você digitou um nome vazio. Tente novamente")
        nome = input("digite o nome do produto: ")
    for ean in produtos:
        if produtos[ean]["nome"] == nome.lower():
            contador += 1
    while contador == 1:
        print("você digitou um nome de um produto já cadastrado no sistema")
        print("tente novamente")
        nome = input("digite o nome do produto: ")
        nome = nome.lower()
        contador = 0
        for ean in produtos:
            if produtos[ean]["nome"] == nome.lower():
                contador += 1


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

