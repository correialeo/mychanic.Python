import requests
from backend.models import ProblemaVeicular
from backend.database import session

def fetch_external_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]:  
            new_problem = ProblemaVeicular(
                problema=post['title'],
                sintoma='Sintoma de exemplo',
                causa='Causa de exemplo',
                solucao=post['body']
            )
            session.add(new_problem)
        session.commit()
        print('Dados externos importados com sucesso.')
    else:
        print('Falha ao obter dados da API externa.')
