import datetime
from src.stages.contracts.transform_contract import TransformContract

transform_contract_mock = TransformContract(
    load_content=[
        {'Name': 'Antioxidante BASS Evita Ranço - 1KG', 'ID': '263', 'URL': 'http:\\/\\/www.adicel.com.br\\/antioxidantes\\/antioxidante-bass-anti-ranco-1kg', 'Price': '45.10', 'extraction_date': datetime.date(2024, 11, 7)},
    ]
)
