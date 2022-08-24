import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

#Qual a média de Customer_Age
print(sales['Customer_Age'].mean())

#sales['Customer_Age'].plot(kind='box', figsize=(14, 6))

#Qual a média de Order_Quantity

print(sales['Order_Quantity'].mean())

sales['Order_Quantity'].plot(kind='hist', figsize=(14, 6))

sales['Order_Quantity'].plot(kind='box', vert=False, figsize=(14, 6))
#plt.show()

#Mostre a qtde de vendas por ano
print(f"Vendas por ano: {sales.groupby('Year').size()}")

sales.groupby('Year').size().plot(kind='bar', figsize=(14, 6))
#plt.show()
#Mostre a qtde de vendas por mês
print(f"Vendas por mês {sales.groupby('Month').size()}")

#Qual país tem maior quantidade de vendas?
print(f"Pais com maior quantidade de vendas: {sales.groupby('Country').size().head(1)}")

sales.groupby('Country').size().plot(kind='bar', figsize=(14, 6))
#plt.show()


#Crie uma lista de cada produto vendido
#Similar a um SELECT DESCRICAO FROM PRODUTO GROUP BY DESCRICAO ...
print(f"Lista de todos produtos vendidos: {sales.groupby('Product')['Product'].head()}")

#sales['Calculated_Date'] = f"{sales['Year']}-{sales['Month']}-{sales['Day']}"

#print(sales['Calculated_Date'].head())



#Quantas vendas foram feitas no Canadá OU França

print(sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0])

#Quantas 'Bike Racks' foram feitas do canadá

print(sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0])

#Quantas compras foram efetuadas em cada estado da França

print(sales.loc[(sales['Country'] == 'France')].groupby('State').size())

#Quantas compras foram efetuadas por categoria?

print(sales.groupby('Product_Category').size())

#Quantas compras foram efetuadas por sub-categorias de Bike

print(sales.loc[(sales['Product_Category'] == 'Bikes')].groupby('Sub_Category').size())

#Qual gênero compra mais?
print(sales['Customer_Gender'].value_counts()[0])

# Quantas vendas foram feitas por homens e com valor maior que 500
print(sales.loc[(sales['Revenue'] >= 500 & (sales['Customer_Gender'] == 'M'))].shape[0])

# top 5 vendas com maior faturamento

print(sales.sort_values(['Revenue'], ascending=False).head(5))

# venda com maior faturamento

print(sales['Revenue'].max())

# Média da coluna Order_Quantity com faturamento maior de 10k

cond = sales['Revenue'] >= 10_000

print(sales.loc[cond, 'Order_Quantity'].mean())

cond = (sales['Year'] == 2016) & (sales['Month'] == 'May')
print(sales.loc[cond].shape[0])