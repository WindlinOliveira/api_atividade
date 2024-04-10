from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=52)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    # print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.nome = 'Windlin'
    pessoa.save()

def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Windlin').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    # altera_pessoa()
    excluir_pessoa()
    consulta_pessoas()
    