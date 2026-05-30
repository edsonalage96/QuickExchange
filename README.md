# QuickExchange - Conversor de Moedas em Python

O QuickExchange e uma aplicacao de linha de comandos simples e robusta desenvolvida em Python para consultar taxas de cambio e realizar conversoes monetarias em tempo real. O projeto consome dados diretamente de uma API publica (AwesomeAPI), consolidando conceitos fundamentais de desenvolvimento de software e integracao de sistemas.

---

## Funcionalidades

- **Consulta em Tempo Real**: Ligacao direta a API externa para obter as cotacoes de mercado mais atualizadas.
- **Suporte Dinamico**: Permite selecionar de forma interativa a moeda de origem e a moeda de destino.
- **Tratamento de Erros**: Validacoes integradas para tratar erros de ligacao, combinacoes de moedas nao suportadas pelo mercado e entradas de dados invalidas por parte do utilizador.
- **Ambiente Local Isolado**: Desenvolvido numa estrutura de pastas limpa e fora de sistemas de sincronizacao em nuvem (como o OneDrive) para garantir a estabilidade da execucao.

---

## Moedas Suportadas

O sistema permite cruzar e converter operacoes entre as 10 moedas mais frequentes e negociadas do mercado:

1. USD (Dolar Americano)
2. EUR (Euro)
3. GBP (Libra Esterlina)
4. JPY (Iene Japones)
5. AUD (Dolar Australiano)
6. CAD (Dolar Canadiano)
7. CHF (Franco Suico)
8. CNY (Yuan Chines)
9. BTC (Bitcoin)
10. BRL (Real Brasileiro)

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca requests**: Para efetuar pedidos HTTP (GET) e integrar o sistema com o servidor da API.
- **Git e GitHub**: Para o controlo de versao profissional e armazenamento do codigo na nuvem.

---

## Como Instalar e Usar

1. **Clonar o repositorio**:
   ```bash
   git clone https://github.com
   cd QuickExchange
   ```

2. **Instalar a biblioteca de integracao**:
   ```bash
   pip install requests
   ```

3. **Executar a aplicacao**:
   ```bash
   python quickexchange.py
   ```

---
Desenvolvido com o proposito de consolidar o consumo de APIs rest, tratamento de dados estruturados em formato JSON e o fluxo correto de versionamento com ramificacoes no Git.
