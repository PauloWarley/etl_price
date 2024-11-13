from src.drivers.get_page import GetPageFromUrl
from src.drivers.get_element import GetElementByXpath
from src.stages.extract import Extract

def test_extract():
    get_page = GetPageFromUrl()
    get_element = GetElementByXpath()
    extract_html = Extract(get_page, get_element)
    url = "https://www.adicel.com.br/antioxidantes/antioxidante-bass-anti-ranco-1kg"
    response = extract_html.extract(url)
    with open("result.response", "w") as f:
        f.write(response.raw_info)

if __name__ == "__main__":
    test_extract()
