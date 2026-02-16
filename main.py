usuarios = []

def cadastrar():
    nome = input('Digite o nome: ')
    usuarios.append(nome)
    print('Usuário cadastrado com sucesso!')

def listar():
    if not usuarios:
        print('Nenhum usuário cadastrado.')
    else:
        print('\nUsuários cadastrados:')
        for u in usuarios:
            print('-', u)

def remover():
    nome = input('Digite o nome para remover: ')
    if nome in usuarios:
        usuarios.remove(nome)
        print('Usuário removido.')
    else:
        print('Usuário não encontrado.')

while True:
    print('\n1 - Cadastrar')
    print('2 - Listar')
    print('3 - Remover')
    print('4 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        remover()
    elif opcao == '4':
        print('Encerrando...')
        break
    else:
        print('Opção inválida!')
