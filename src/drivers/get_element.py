from typing import List, Dict
from bs4 import BeautifulSoup

class GetElementByXpath ():
    
    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {url:self.url}
    

    def get_from_html(self, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, "html.parser")
        
        product_name_list = soup.find(class_="fixed-info")
        product_name_list_items = product_name_list_items.find_all('product-name')

        essential_information = [] #Em teoria, pega a célula inteira (fixed-info) para ser filtrada
        for product_name in product_name_list_items:
            names = product_name.contents[0]
            self.url + product_name.get('href')
            essential_information.append({
                "name": names,
                "link": self.url
            })

        return essential_information
