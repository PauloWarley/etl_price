from typing import List, Dict
from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TransformContract
from src.errors.transform_error import TransformError
from bs4 import BeautifulSoup
from lxml import etree 


class TransformRawData:

    def transform(self, extract_contract: ExtractContract, scrap_config: dict) -> TransformContract:
        try:  
            transformed_information = self.__filter_and_transform_data(extract_contract, scrap_config)
            transformed_data_contract = TransformContract(
                load_content=transformed_information
            )
            return transformed_data_contract
        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter_and_transform_data(self, extract_contract: ExtractContract, scrap_config: dict) -> List[Dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_info
        link = extract_contract.url
        soup = BeautifulSoup(data_content, "html.parser")

        dom = etree.HTML(str(soup)) 
        product_name = dom.xpath(scrap_config["product_name"])[0].text
        product_id = dom.xpath(scrap_config["product_id"])[0].text
        price = dom.xpath(scrap_config["price"])[0].text

        transformed_information = []
        
        transformed_data = self.__transform_data(product_name, product_id, link, price)
        transformed_data["extraction_date"] = extraction_date
        transformed_information.append(transformed_data)

        return transformed_information

    @classmethod
    def __transform_data(cls, product_name: str, product_id: str, link: str, price: str) -> Dict:
        return {
            "Name": product_name,
            "ID": product_id,
            "URL": link,
            "Price": price
        }
