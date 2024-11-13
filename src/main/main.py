from src.stages.extract import Extract
from src.stages.transform import TransformRawData
from src.stages.load import LoadData
from src.drivers.get_page import GetPageFromUrl
from src.drivers.get_element import GetElementByXpath

class MainPipeline:
    def __init__(self) -> None:
        self.__extract = Extract
        self.__transform = TransformRawData
        self.__load = LoadData

    def run_pipeline(self) -> None:
        links_adicel = [
            "https://www.adicel.com.br/antioxidantes/antioxidante-de-hamburguer-1-kg",
            "https://www.adicel.com.br/antioxidantes/antioxidante-de-hamburguer-1-kg",
            "https://www.adicel.com.br/antioxidantes/antioxidante-de-hamburguer-1-kg",
            "https://www.adicel.com.br/antioxidantes/antioxidante-de-hamburguer-1-kg",
            "https://www.adicel.com.br/antioxidantes/antioxidante-de-hamburguer-1-kg",
            "https://www.adicel.com.br/antioxidantes/antioxidante-de-hamburguer-1-kg",
        ]
        # links_adicel = "https://www.mercadolivre.com.br/violo-eletroacustica-giannini-performance-gsf-3-ceq-para-destros-translucent-dark-wine-madeira-tecnica-verniz-brilhante/p/MLB15307281?pdp_filters=item_id%3AMLB3878426683#polycard_client=recommendations_home_navigation-trend-recommendations&reco_backend=machinalis-homes-univb&wid=MLB3878426683&reco_client=home_navigation-trend-recommendations&reco_item_pos=2&reco_backend_type=function&reco_id=cba3a160-d168-4a47-926a-2b80ebe9392f&sid=recos&c_id=/home/navigation-trend-recommendations/element&c_uid=1c628165-7eed-43a7-a7b3-2ff074ade93c"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
        
        for url in links_adicel:
        
            extract=self.__extract(GetPageFromUrl, GetElementByXpath, headers=headers)
            extract_data=extract.extract(url=url)

            scrap_config = {
                "product_name": "//h1[@class='product-name']",
                "product_id": "//span[@id='product-reference']",
                "price": '//strong[@class="PrecoPrincipal"]',
            }
            # scrap_config = {
            #     "product_name": "//h1[@class='ui-pdp-titlee']",
            #     "product_id": "//h1[@class='ui-pdp-titlee']",
            #     "price": '//span[@class="andes-money-amount__fraction"]',
            # }

            transform = self.__transform()
            transform_data = transform.transform(extract_data, scrap_config)
            print(transform_data)
            load = self.__load(data=transform_data, filepath="./adicel-scrap.xlsx")
            
            load.save_to_excel()

pipeline=MainPipeline()
pipeline.run_pipeline()