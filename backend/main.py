from backend.api import fetch_external_data
from backend import crud


def get_user_choice():
    valid = False
    while not valid:
        try:
            escolha = int(input('''
            Digite 1 para Registrar
            Digite 2 para Ler
            Digite 3 para Atualizar
            Digite 4 para Remover
            Digite 5 para Exportar para JSON
            Digite 6 para Importar Dados Externos
            Digite 7 para Sair: '''))
            if 1 <= escolha <= 7:
                valid = True
            else:
                print('Opção inválida. Tente novamente!')
        except ValueError:
            print('Por favor, insira um número inteiro.')
    return escolha

if __name__ == "__main__":
    opcao = 0
    while opcao != 7:
        opcao = get_user_choice()
        if opcao == 1:
            crud.create()
        elif opcao == 2:
            crud.read()
        elif opcao == 3:
            crud.update()
        elif opcao == 4:
            crud.delete()
        elif opcao == 5:
            crud.export_to_json()
        elif opcao == 6:
            fetch_external_data()
        elif opcao == 7:
            print('Saindo do programa...')
            break
