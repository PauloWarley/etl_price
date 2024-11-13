import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from src.errors.load_error import LoadError
from datetime import datetime

class LoadData:
    def __init__(self, filepath='data_scraping.xlsx', data : TransformContract = {}):
        self.filepath = filepath
        self.data = data

    def save_to_excel(self):
        try:
            df = pd.DataFrame().from_dict(self.data.load_content) #criando dataframe

            try: #tenta carregar dados existentes e novos
                existing_data = pd.read_excel(self.filepath)
                df = pd.concat([existing_data, df], ignore_index=True)
            except FileNotFoundError: #cria um arquivo novo se precisar
                pass

            df.to_excel(self.filepath, index=False) #salva o df e inclui dados novos
            print(f"Dados carregados em {self.filepath} com sucesso!")

        except Exception as exception: #caso haja erro
            raise LoadError(f"Erro ao carregar dados para a planilha: {str(exception)}") from exception

if __name__ == "__main__":
    data = {
        'Name': 'Antioxidante BASS Evita Ranço - 1KG',
        'ID': '263',
        'URL': 'http://www.adicel.com.br/antioxidantes/antioxidante-bass-anti-ranco-1kg',
        'Price': '45.10',
        'extraction_date': datetime.now().strftime("%d/%m/%Y %H:%M:%S") #como os dados virao do contrato
    }

    loader = LoadData(data = data)
    loader.save_to_excel()
