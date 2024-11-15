from datetime import datetime
from src.drivers.get_page import GetPageFromUrl
from src.drivers.get_element import GetElementByXpath
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

class Extract:
    def __init__(self, get_page: GetPageFromUrl, get_element: GetElementByXpath, headers: dict) -> None:
        self.__get_page = get_page(headers)
        self.__get_element = get_element
    
    def extract(self, url: str) -> ExtractContract:
        try:
            html = self.__get_page.fetch_page(url)
            return ExtractContract(
                raw_info=html,
                extraction_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S") ,
                url=url
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception
