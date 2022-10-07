import yfinance


dados = yfinance.Ticker("MGLU3.SA")
tabela = dados.history("6mo")
print(tabela)