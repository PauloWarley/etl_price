from src.drivers.get_page import GetPageFromUrl
from src.drivers.get_element import GetElementByXpath

class Main:
    
    def __init__(self, get_page: GetPageFromUrl, get_element: GetElementByXpath) -> None:
        self.__get_page = get_page
        self.__get_element = get_element
    
    def run_main(self) -> None:
        url = "https://www.adicel.com.br/antioxidantes/antioxidante-bass-anti-ranco-1kg"
        get_page = self.__get_page()
        html = get_page.fetch_page(url = url)
        f = open("result.html", "w")
        f.write(html)
        
main = Main(GetPageFromUrl, GetElementByXpath)
main.run_main()
