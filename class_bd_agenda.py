import mysql.connector
from class_contato import Contato


class DBAgenda:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='agenda'
        )
        self.meu_cursor = self.conexao.cursor()

    def salvar_contatos(self, cod, nome, telefone, email):
        obj_contato = Contato(cod, nome, telefone, email)
        comando_sql = f'insert into Contatos (nome, telefone, email) value ("{obj_contato.nome}","{obj_contato.telefone}","{obj_contato.email}") '
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
        
    def listar_contatos(self):
        comando_sql = 'select * from Contatos'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def Mudar_contatos(self, atributo,valor, cod):
        comando_sql = f'update Contatos ' \
                      f'set {atributo} = "{valor}"' \
                      f' where id = "{cod}"'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def exclui_contato(self, cod):
        for i in range(len(self.listaContatos)):
            if cod == self.listaContatos[i].cod:
                del self.listaContatos[i]
            else:
                print('Codigo de Contato não existe!')