import pandas as pd
import matplotlib.pyplot as plt


microdados_enem = pd.read_csv('/run/media/jhonata/_home/MICRODADOSENEM.csv', sep=';', encoding='ISO-8859-1') 
# Leitura dos dados armazenados no arquivo .csv
print(microdados_enem.head())
# Amostragem bruta dos dados
print(microdados_enem)
# Também pode-se visualizar os dados chammando apenas por sua variável
