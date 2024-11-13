from typing import List, Dict
from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TransformContract
from src.errors.transform_error import TransformError

class TransformRawData:

    def transform(self, extract_contract: ExtractContract) -> TransformContract:
        try:  
            transformed_information = self.__filter_and_transform_data(extract_contract)
            transformed_data_contract = TransformContract(
                load_content=transformed_information
            )
            return transformed_data_contract
        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter_and_transform_data(self, extract_contract: ExtractContract) -> List[Dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_info
        transformed_information = []

        for data in data_content:
            transformed_data = None
            product_name = data["nameProduct"]
            product_id = data["idProduct"]
            link = data["urlProduct"]
            price = data["price"]
            
            transformed_data = self.__transform_data(product_name, product_id, link, price)
            transformed_data["extraction_date"] = extraction_date
            print(transformed_data)
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
