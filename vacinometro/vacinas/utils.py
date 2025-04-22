import requests

def get_dados_vacinas():
    url = "https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2025?limit=100&offset=1"
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    
    try:
        data = response.json()
        return data["doses_aplicadas_pni"]  # 👈 Pega só a lista com os registros
    except Exception as e:
        print(f"Erro ao processar JSON: {e}")
        return []
