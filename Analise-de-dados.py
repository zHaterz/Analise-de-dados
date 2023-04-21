# Meta de venda para cada vendedor é 55 mil 

#passo 1 - passar por todas as planilia 
 #Verificar se algum valor na coluna de Vendas, dos arquivos passa de 55 mil, caso passe o vendendo 
 # deve ganhar um bonificação!
 
 #  Valor -> 55 mil (Envia sms para o telefone)
 
 
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1c4b214001e13359ed587278477cf1f4"
# Your Auth Token from twilio.com/console
auth_token  = "43aa7d0887c9b504c87349e65021c1e6"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março', 'abril', 'maio', 'junho']
tabela_total = pd.DataFrame()

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'plan/{mes}.xlsx')
    
    if (tabela_vendas['Vendas'] > 55000).any():
      vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
      vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
      message = client.messages.create(
    to="+5521983854412", 
    from_="+16073604246",
    body=f"Olá o Vendedor:{vendedor}, alcançou a meta de {vendas:,.2f} no mês de {mes}!")
        