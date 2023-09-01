#PhihsingTank https://phishtank.org/
import requests
from bs4 import BeautifulSoup

url = "https://phishtank.org/"

def scraping_phishtank():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra todas as tags <tr> na página
    tr_tags = soup.find_all('tr')
    
    # Inicializa uma lista vazia para armazenar os dicionários
    data_list = []
    
    # Itera sobre as tags <tr> encontradas, ignorando a primeira (cabeçalho)
    for tr in tr_tags[1:]:
        # Pega todas as tags <td> na linha
        td_tags = tr.find_all('td')
        
        # Verifica se existem pelo menos 3 tags <td>
        if len(td_tags) >= 3:
            # Cria um dicionário para armazenar os dados
            data_dict = {
                'ID': td_tags[0].text.strip(),
                'Url': td_tags[1].text.strip(),
                'Submitted by': td_tags[2].text.strip()
            }
            
            # Adiciona o dicionário à lista de dados
            data_list.append(data_dict)
    
    # Imprime a lista de dicionários
    for data in data_list:
        print(data)

scraping_phishtank()
