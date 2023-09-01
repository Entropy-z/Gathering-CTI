#Ranwomlook https://www.ransomlook.io/recent

import requests
from bs4 import BeautifulSoup

url = "https://www.ransomlook.io/recent"
USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0 uacq"
headers = {'User-Agent': USERAGENT}

def scraping_ransom():
    response = requests.get(url=url, headers=headers)
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
