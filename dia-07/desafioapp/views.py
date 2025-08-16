from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    page = int(request.GET.get("page", 1))
    proxima = page + 1
    url = f"https://last-airbender-api.fly.dev/api/v1/characters?page={page}"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        
        # Corrige IDs entre páginas
        for index, item in enumerate(dados, start=(page - 1) * 20 + 1):
            item["id"] = index
            
        return render(request, "desafioapp/index.html", {
            "dados": dados,
            "pagina": page,
            "proxima": proxima,
        })
    else:
        return HttpResponse(f"Erro na requisição: {response.status_code}")
