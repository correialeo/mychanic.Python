from backend.models import ProblemaVeicular
from backend.database import session

def create():
    problema = input('Qual é o problema? ')
    sintoma = input('Qual é o sintoma do problema? ')
    causa = input('Qual é a causa do problema? ')
    solucao = input('Qual é a solução para o problema descrito acima? ')

    new_problem = ProblemaVeicular(
        problema=problema,
        sintoma=sintoma,
        causa=causa,
        solucao=solucao
    )
    session.add(new_problem)
    session.commit()
    print('Novo dado inserido com sucesso')

def read():
    problemas = session.query(ProblemaVeicular).all()
    if not problemas:
        print("Não existem dados registrados.")
    for problema in problemas:
        print(problema)

def update():
    id = int(input('Digite o ID do problema que deseja alterar: '))
    problema = session.query(ProblemaVeicular).filter_by(id=id).first()
    if not problema:
        print('Nenhum ID foi encontrado')
    else:
        print('Dado atual:', problema)

        novo_problema = input('Digite o problema (deixe em branco para manter o atual): ')
        if novo_problema:
            problema.problema = novo_problema

        nova_causa = input('Digite a causa (deixe em branco para manter a atual): ')
        if nova_causa:
            problema.causa = nova_causa

        novo_sintoma = input('Digite o sintoma (deixe em branco para manter o atual): ')
        if novo_sintoma:
            problema.sintoma = novo_sintoma

        nova_solucao = input('Qual é a solução? (deixe em branco para manter a atual): ')
        if nova_solucao:
            problema.solucao = nova_solucao

        session.commit()
        print('Dados atualizados com sucesso.')

def delete():
    id = int(input('Qual é o ID do problema que deseja deletar? '))
    problema = session.query(ProblemaVeicular).filter_by(id=id).first()
    if not problema:
        print('Não há problemas com esse ID')
    else:
        session.delete(problema)
        session.commit()
        print('Dado excluído com sucesso')


import json

def export_to_json():
    problemas = session.query(ProblemaVeicular).all()
    data = [
        {
            'id': problema.id,
            'problema': problema.problema,
            'sintoma': problema.sintoma,
            'causa': problema.causa,
            'solucao': problema.solucao
        }
        for problema in problemas
    ]
    with open('problemas_veiculares.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('Dados exportados para problemas_veiculares.json com sucesso.')
