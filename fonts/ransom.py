#Ranwomlook https://www.ransomlook.io/recent

import requests
from bs4 import BeautifulSoup

URL = "https://www.ransomlook.io/recent"

def scraping_ransom(user_agent):
    headers = {'User-Agent': user_agent}
    response = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tag_main = soup.find_all('tr')
    
    data_list = []
    
    for tr in tag_main[1:]:
        td_tags = tr.find_all('td')
        
        if len(td_tags) >= 3:
            data_dict = {
                'Date': td_tags[0].text.strip(),
                'Victim': td_tags[1].text.strip(),
                'Group': td_tags[2].text.strip()
            }
            data_list.append(data_dict)
    
    return data_list
    

for i in scraping_ransom():
    print (i)
