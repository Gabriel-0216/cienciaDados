import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

#Mostra o top 5 registros para visualização rápida
print(sales.head())

#Informações basica de quantidade de linhas x colunas
print(sales.shape)

#Análise das colunas
print(sales.info())
print(sales.describe())

#Análise numerica e visualização

print(sales['Unit_Cost'].describe())

#Média

print(sales['Unit_Cost'].mean())

#Mediana
print(sales['Unit_Cost'].median())

#Moda
print(sales['Unit_Cost'].mode())

print(sales['Customer_Age'].mean())

#Análise categorica e visualização



