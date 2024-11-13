from src.stages.contracts.mocks.extract_contract_mock import extract_contract_mock
from src.stages.contracts.transform_contract import TransformContract
from src.stages.transform import TransformRawData

def test_transform():
    
    transform_raw_data = TransformRawData()
    transformed_data_contract = transform_raw_data.transform(extract_contract_mock)
    print()

    assert isinstance(transformed_data_contract, TransformContract)
    assert "Name" in transformed_data_contract.load_content[0]
    assert "ID" in transformed_data_contract.load_content[0]
    assert "URL" in transformed_data_contract.load_content[0]
    assert "Price" in transformed_data_contract.load_content[0]
    assert "extraction_date" in transformed_data_contract.load_content[0]

if __name__ == "__main__":
    test_transform()
