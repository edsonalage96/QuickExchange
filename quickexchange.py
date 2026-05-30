import requests

MOEDAS = {
    "1": "USD", "2": "EUR", "3": "GBP", "4": "JPY", "5": "AUD",
    "6": "CAD", "7": "CHF", "8": "CNY", "9": "BTC", "10": "BRL"
}

def exibir_moedas():
    print("\nMoedas Disponiveis:")
    print("1. USD (Dolar Americano)   2. EUR (Euro)              3. GBP (Libra Esterlina)")
    print("4. JPY (Iene Japones)      5. AUD (Dolar Australiano) 6. CAD (Dolar Canadiano)")
    print("7. CHF (Franco Suico)      8. CNY (Yuan Chines)       9. BTC (Bitcoin)")
    print("10. BRL (Real Brasileiro)")

def selecionar_moeda(mensagem):
    while True:
        exibir_moedas()
        opcao = input(mensagem).strip()
        if opcao in MOEDAS:
            return MOEDAS[opcao]
        print("Opcao invalida. Escolha um numero de 1 a 10.")

def converter_moedas():
    print("\n--- Configurar Conversao ---")
    origem = selecionar_moeda("Escolha a moeda de ORIGEM (numero): ")
    destino = selecionar_moeda("Escolha a moeda de DESTINO (numero): ")

    if origem == destino:
        print("A moeda de origem nao pode ser igual a moeda de destino.")
        return

    # Endpoint oficial e seguro da API externa
    url = f"https://economia.awesomeapi.com.br/json/last/{origem}-{destino}"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 404:
            print(f"Combinacao {origem} para {destino} nao e suportada.")
            return

        dados = resposta.json()
        chave_api = f"{origem}{destino}"
        
        if chave_api in dados:
            info = dados[chave_api]
            cotacao = float(info["bid"])
            print(f"\n--- Cotacao Atual ---")
            print(f"1 {origem} = {cotacao:.4f} {destino}")
            
            try:
                qtd = float(input(f"\nQuantos {origem} deseja converter? "))
                print(f"Resultado: {qtd:.2f} {origem} = {qtd * cotacao:.4f} {destino}")
            except ValueError:
                print("Introduza um valor numerico valido.")
        else:
            print("Dados nao encontrados na resposta da API.")
    except Exception as e:
        print("Erro de conexao:", e)

def menu():
    while True:
        print("\n--- QuickExchange ---")
        print("1. Realizar Conversao \n2. Sair")
        opcao = input("Opcao: ").strip()
        if opcao == "1": converter_moedas()
        elif opcao == "2": break
        else: print("Opcao invalida.")

if __name__ == "__main__":
    menu()
