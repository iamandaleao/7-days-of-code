import json
import asyncio
import requests
from googletrans import Translator

async def traduzir(text, dest='pt'):
    translator = Translator()
    result = await translator.translate(text, dest=dest)
    return result.text

def personagens():
    url = 'https://last-airbender-api.fly.dev/api/v1/characters'
    response = requests.get(url)

    if response.status_code == 200:
        personagem = response.json() # Converte para dicionário/lista Python
        for p in personagem:
            affiliacao = p.get('affiliation', '')
            p['affiliacao_traduzida'] = asyncio.run(traduzir(affiliacao))
            nome = p.get('name', '')
            p['name_traduzido'] = asyncio.run(traduzir(nome))
            
        return json.dumps(personagem, indent=4)

    else:
        print(f"Erro na requisição: {response.status_code}")


print(personagens())
