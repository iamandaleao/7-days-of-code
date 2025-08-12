import json
import requests

url = "https://last-airbender-api.fly.dev/api/v1/characters"

# Faz a requisição GET
response = requests.get(url)

#Verifica se deu tudo certo (status 200= ok)
if response.status_code == 200:
  dados = response.json() # Converte para dicionário/lista Python
  print(json.dumps(dados, indent=4))
else:
  print(f"Erro na requisição: {response.status_code}")

