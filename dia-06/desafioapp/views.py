from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# Create your views here.
def index(request):
    url = "https://last-airbender-api.fly.dev/api/v1/characters"

    # Faz a requisição GET
    response = requests.get(url)

    # Verifica se deu tudo certo (status 200 = ok)
    if response.status_code == 200:
        dados = response.json()  # Converte para dicionário/lista Python
        dados = [{**p, "id": p["_id"]} for p in dados]
        return render(request, "desafioapp/index.html", {"dados":dados})
    else:
        print(f"Erro na requisição: {response.status_code}")
        return HttpResponse(f"Erro na requisição: {response.status_code}")
