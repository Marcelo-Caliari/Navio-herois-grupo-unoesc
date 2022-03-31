print('Insira o login administrador')
auth = False

while auth == False:
    name = input("Insira o seu nome: ")
    password = input("Insira a sua senha: ")
    if(name == 'admin' and password == 'admin'):
        print('você está logado')
        auth = True
    else:
        print('Você não está logado')
        auth = False
  

