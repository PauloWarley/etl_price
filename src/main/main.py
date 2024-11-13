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
        links_adicel = "https://www.adicel.com.br/antioxidantes/antioxidante-bass-anti-ranco-1kg"
        user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
        extract=self.__extract (GetPageFromUrl, GetElementByXpath, user_agent=user_agent)
        extract_data=extract.extract(url=links_adicel)
        print(extract_data)
        #self.__transform()
        #self.__load()

pipeline=MainPipeline()
pipeline.run_pipeline()