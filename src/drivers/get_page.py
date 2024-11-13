import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GetPageFromUrl:
    
    def __init__(self, headers) -> None:
        self.headers = headers
    
    def fetch_page(self, url):
        try: #tantando com requests
            response = requests.get(url, headers=self.headers)

            response.raise_for_status()  #exceção em caso de erro HTTP
            print("Conteúdo obtido com requests.")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Requests falhou: {e}. Tentando com Selenium...")
            return self.from_selenium(url) #alternando pra selenium
    
    def from_selenium(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  #navegador em segundo plano
        chrome_options.add_argument(f"user-agent={self.headers["User-Agent"]}")

        driver = webdriver.Chrome(options=chrome_options) #configura automaticamente
        try:
            driver.get(url)
            page_source = driver.page_source
            print("Conteúdo obtido com Selenium.")
            return page_source
        finally:
            driver.quit()  #fecha o driver
