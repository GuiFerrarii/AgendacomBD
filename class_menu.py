from class_bd_agenda import DBAgenda


class Menu:
    def __init__(self):
        agenda = DBAgenda()

        while True:
            entrada=input(('1 - Novo Cadastro\n2 - Listar Contatos\n0 - Sair\n3 - Mudar contato\n4 - deletar contato ->'))
            if entrada == '1':
                cod = None
                nome = input('Digite o Nome: ')
                telefone = input('Digite o Telefone: ')
                email = input('Digite seu email:')
                agenda.salvar_contatos(cod, nome, telefone, email)


            elif entrada == '2':
                agenda.listar_contatos()


            elif entrada == '3':
                cod = int(input('Informe o código do contato'))
                valor = input('Entre com o novo nome')
                atributo = 'nome'
                agenda.Mudar_contatos(atributo, valor, cod)


            elif entrada == '4':
                agenda.exclui_contato()


            elif entrada == '0':
                break
            else:
                print('Leia as opções burrão!!')