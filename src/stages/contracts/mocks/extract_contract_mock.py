from datetime import date
from src.stages.contracts.extract_contract import ExtractContract

extract_contract_mock = ExtractContract(
    raw_info=[
        {"pageTitle":"Antioxidante Bass (Anti ran\u00e7o) - 1kg | Adicel Ingredientes","pageCategory":"Produto","event":"","siteSearchFrom":"https:\/\/www.adicel.com.br\/loja\/busca.php?loja=755044&palavra_busca=bass","idProduct":"263","nameProduct":"Antioxidante BASS Evita Ran\u00e7o - 1KG","category":"Antioxidantes","idCategory":"9","priceSell":"45.10","promotion":"NO","price":"45.10","brand":"Adicel","reference":"288","model":"","availability":"YES","availabilityDetails":"Imediata","urlImage":"https:\/\/images.tcdn.com.br\/img\/img_prod\/755044\/antioxidante_bass_evita_ranco_1kg_263_1_330cceaf073f9266877db626dd080bbd.jpg","urlProduct":"http:\/\/www.adicel.com.br\/antioxidantes\/antioxidante-bass-anti-ranco-1kg","listSku":[],"characteristcs":[{"description":"Segmento","value":"Biscoitos"}],"priceSellDetails":[{"name":"","installment.months":"1","installment.amount":"45.10"}],"EAN":"7898329370538","breadcrumbDetails":[{"id":"1","name":"Aditivos Alimentares","level":1},{"id":"9","name":"Antioxidantes","level":2}],"freeShipping":"NO","hot":"NO","additionalButton":"NO","release":"NO","rating":{"count":"1","average":"5"},"breadcrumb":"P\u00e1gina Inicial > Aditivos Alimentares > Antioxidantes"}
    ],
    extraction_date=date.today()
)