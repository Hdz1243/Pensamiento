import math
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo(amount, avg_return, volatility, iterations):
  path = [amount]
  for i in range(iterations):
    z = np.random.normal(0,1)
    amount = amount * math.exp((avg_return-volatility**2/2)+volatility*z)
    path.append(amount)
  return path

resultados = []

amount = int(input("Inserta la cantidad inicial de dinero: "))
avg_return = float(input("Inserta el promedio de retorno anual (en porcentaje): "))/100
volatility = float(input("Inserta la volatilidad anual (en porcentaje): "))/100
iterations = int(input("Inserta cuantos años vas a dejar invertido ese dinero: "))
years = [i for i in range(iterations+1)]

for i in range(1000):
  resultados.append(monte_carlo(amount, avg_return, volatility, iterations))

for i in range(len(resultados)):
  plt.plot(years, resultados[i])

plt.xlabel('Years')
plt.ylabel('Amount')
plt.title('Monte Carlo Simulation')
plt.show()

resultados_np = np.array([resultados[i][-1] for i in range(len(resultados))])
r1 = np.percentile(resultados_np, 10)
r2 = np.percentile(resultados_np, 50)
r3 = np.percentile(resultados_np, 90)
print(f'En el peor de los casos (percentil 10) terminaste con ${r1:,.2f}')
print(f'En el caso esperado (percentil 50) terminaste con ${r2:,.2f}')
print(f'En el mejor de los casos (percentil 90) terminaste con ${r3:,.2f}')

