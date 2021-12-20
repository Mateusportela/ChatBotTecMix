

#importando a biblioteca numpy.
import numpy as np


#pegando arquivo 'testecsv.csv' e armazenando na variavel.
calorie_stats = np.genfromtxt(r"C:\Users\Windows10\Desktop\csv\testecsv.csv",delimiter=",")
#print(calorie_stats)

#abrindo o arquivo 'testecsv.csv
with open(r"C:\Users\Windows10\Desktop\csv\testecsv.csv") as teste_csv:
  first_line = teste_csv.read()
print(first_line)

#media de caloria do produto.
average_calories = np.mean(calorie_stats)
print(average_calories)

# usando o metodo .sort para ordenar os numeros em ordem crescente e ver qual numero pode alterar a real media das amostras. ex:49,50,52 e 90.(O '90' difere muito dos valores das amostras.)
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

# usando o metodo .median para encontrar a madiana da matriz.
median_calories = np.median(calorie_stats)
print(median_calories)


#usando o metodo .percentile para descobrir o produto que possue a menor caloria e que seja acima de 60 calorias.  
nth_percentile = np.percentile(calorie_stats , 4)
print(nth_percentile)


#encontrar a porcentagem de produtos que possuem uma caloria acima de 60. Nesse caso 96% dos produtos tem caloria > 60.
more_calories = np.mean(calorie_stats > 60)
print(str(more_calories)[2:4] + '%') 
print(more_calories)


#usando o metodo .std para encotrar o desvio padrao e analisar a dispersao das amostras.
calorie_std=np.std(calorie_stats)
print(calorie_std)

texto = "Analisando a amostra de 77 produtos, o CrunchieMunchies possui menos calorias do que 96% da concorrencia."
print(texto)