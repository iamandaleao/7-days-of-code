# Avatar API – Consumo com Python

Este projeto faz parte do programa **#7DaysOfCode**, uma iniciativa da Alura para desafiar e aprimorar habilidades em programação ao longo de 7 dias.  
O foco é praticar diariamente, aplicar conhecimentos em desafios reais e construir projetos para o portfólio.  

Neste repositório, registro minha jornada no desafio de Python para backend, consumindo APIs REST e desenvolvendo aplicações práticas.

##  Cronograma dos 7 Dias

| Dia  | Data      | Desafio / Tema                                     |
|-------|-----------|---------------------------------------------------|
| 1     | 09/08/2025| Consumir API REST (Avatar API) usando Python      |
| 2     | 10/08/2025| [Próximo desafio - descrição resumida]            |
| 3     | 11/08/2025| [Próximo desafio - descrição resumida]            |
| 4     | 12/08/2025| [Próximo desafio - descrição resumida]            |
| 5     | 13/08/2025| [Próximo desafio - descrição resumida]            |
| 6     | 14/08/2025| [Próximo desafio - descrição resumida]            |
| 7     | 15/08/2025| Finalização e integração dos conhecimentos        |

*Obs: Os temas dos próximos dias serão atualizados conforme os desafios forem liberados.*

## Tecnologias Utilizadas

- **Python 3.13.5**  
- **Requests 2.28.2**  
- Ferramentas adicionais sugeridas: Visual Studio Code, Postman ou Insomnia.

##  Instalação e Configuração

### Criar e ativar ambiente virtual (opcional, recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### Instale as dependências
`pip install requests`

### Como Executar
`python main.py`

### API Utilizada
Acesse a API [Last Airbender API](https://last-airbender-api.fly.dev/api/v1/characters) para obter informações dos personagens.

## Exemplo de Uso
```python
import requests

url = "https://last-airbender-api.fly.dev/api/v1/characters"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print(f"Erro na requisição: {response.status_code}")
```
