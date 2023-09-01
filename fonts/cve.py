import requests
from bs4 import BeautifulSoup
from typing import List, Dict

PAGES = [0, 20, 40, 60] # page 1 = 0 | page 2 = 20 | page 3 = 40 | page 4 = 60
USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0 uacq"

def scraping_CVEs() -> List[Dict] :
    data_list = []
    
    headers = {'User-Agent': USERAGENT}
    for pg in PAGES:
        url = f"https://nvd.nist.gov/vuln/search/results?isCpeNameSearch=false&results_type=overview&form_type=Basic&search_type=all&startIndex={pg}"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for i in range(0, 20):
            iter_tag = f'vuln-row-{i}'
            tag_main = soup.find_all('tr', attrs={'data-testid': iter_tag})
            
            vuln_data:Dict = {}  
            
            cve_tags = [cve_tag.get_text() for second_main in tag_main for cve_tag in second_main.find_all('a', text=lambda text: text and text.startswith('CVE'))]
            published_tags = [published_tag.get_text() for second_main in tag_main for published_tag in second_main.find_all('span', attrs={'data-testid': f'vuln-published-on-{i}'})]
            summary_tags = [summary_tag.get_text() for second_main in tag_main for summary_tag in second_main.find_all('p', attrs={'data-testid': f'vuln-summary-{i}'})]
            
            vuln_data['CVE'] = cve_tags[0] if cve_tags else ''
            vuln_data['Published'] = published_tags[0] if published_tags else ''
            vuln_data['Description'] = summary_tags[0] if summary_tags else ''
            
            data_list.append(vuln_data)  
    return data_list 
