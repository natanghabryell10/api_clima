import requests

# insatle a biblioteca pip install requests
# Para utilizar este projeto, você precisa de uma API KEY do OpenWeather.
# Crie uma conta em https://openweathermap.org/ e gere sua chave.
# Depois, substitua o valor abaixo pela sua API KEY.


API_KEY = "coloque_sua_chave_aqui"

def buscar_clima(cidade):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        resposta = requests.get(url)

        if resposta.status_code != 200:
            print("Erro: cidade não encontrada ou problema na API.")
            return

        dados = resposta.json()

        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]

        print(f"\nClima em {cidade}:")
        print(f"Temperatura: {temp}°C")
        print(f"Condição: {descricao}")

    except Exception as e:
        print("Erro:", e)


while True:
    print("\n=== CONSULTA DE CLIMA ===")
    cidade = input("Digite uma cidade (ou 'sair'): ")

    if cidade.lower() == "sair":
        print("Encerrando...")
        break

    buscar_clima(cidade)
