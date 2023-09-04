#PhihsingTank https://phishtank.org/
import requests
from bs4 import BeautifulSoup

url = "https://phishtank.org/"

def scraping_phishtank(user_agent):
    headers = {'User-Agent': user_agent}
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tr_tags = soup.find_all('tr')
    
    data_list = []
    for tr in tr_tags[1:]:
        td_tags = tr.find_all('td')
        
        if len(td_tags) >= 3:
            data_dict = {
                'ID': td_tags[0].text.strip(),
                'Url': td_tags[1].text.strip(),
                'Submitted by': td_tags[2].text.strip()
            }
            
            data_list.append(data_dict)
    
    for data in data_list:
        print(data)

scraping_phishtank()
