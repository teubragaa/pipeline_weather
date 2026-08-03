import requests  # Biblioteca para fazer requisições HTTP
import json  # Biblioteca para trabalhar com arquivos JSON
from pathlib import Path # Biblioteca para manipular caminhos de arquivos

import logging # Biblioteca para registrar mensagens do programa
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

def extract_data(url: str) -> list: # Função que recebe uma URL e retorna os dados
    response = requests.get(url) # Faz uma requisição para a URL
    data = response.json() # Converte a resposta para formato JSON (dicionário)

    if response.status_code != 200:   # Verifica se a requisição deu erro
        logging.error(f"Erro na requisicao")
        return []   

    if not data:
        logging.warning(f"No data encontrado.")
        return []   

    output_path = 'data/weather_data.json'  # Caminho onde o arquivo será salvo
    output_dir = Path(output_path).parent  # Pega apenas a pasta ("data")
    output_dir.mkdir(
        parents=True,     # Cria pastas intermediárias se necessário
        exist_ok=True)    # Não gera erro se a pasta já existir
 
    with open(output_path, 'w') as f:  # Abre o arquivo para escrita 'w'
        json.dump(
            data,           # Dados que serão gravados
            f,              # Arquivo onde serão gravados
            indent=4)        # Deixa o JSON formatado (mais bonito)

    logging.info(f"Data successfully extracted and saved to {output_path}.")
    return data
