import numpy as np 
import math as math
import matplotlib.pyplot as plt

"""
# 1.
# a. Probabilitatea ca ambii copii sa fie fete daca cel mare e fata

CopilMare = 1
cnt = 0
for i in range(10000):
    nrFete = 1
    CopilMic = np.random.random()
    if CopilMic > 1/2:
        nrFete = 2
    if nrFete == 2:
        cnt +=1
P = cnt/10000
print(P)

# b. Probabilitatea ca ambii copii sa fie fete daca cel putin unul e fata

cnt = 0
nr = 0
while nr < 10000:
    nrFete = 0
    CopilMare = np.random.random()
    CopilMic = np.random.random()
    if CopilMic > 1/2:
        nrFete +=1
    if CopilMare > 1/2:
        nrFete +=1
    if nrFete == 2:
        cnt +=1
    if nrFete != 0:
        nr += 1
P = cnt/10000
print(P)
"""

# 2.

"""
def sim(k, n, nr):
    cnt = 0
    for i in range(nr):
        cap = 0
        for i in range(n):
            rez = np.random.random()
            if rez < 1/2:
                cap += 1
        if cap == k:
            cnt += 1
    Prob = cnt / nr
    return Prob
k = 29
n = 50
nr = 10000
ProbT = (math.factorial(n)/math.factorial(k)/math.factorial(n - k)) * (1/2) ** k * (1 - 1/2) ** (n - k) 
ProbS = sim(k, n, nr)
print(ProbT)
print(ProbS)
Err = abs(ProbT - ProbS)
print(Err)
"""

# 3. 
"""
a = 0.2
b = 0.6
n_values = [10000, 50000, 100000, 500000, 1000000, 5000000]
results = []
for n in n_values:
    sample = np.random.uniform(0, 1, size=n)
    proportion_in_interval = np.sum((sample > a) & (sample < b)) / n
    results.append(proportion_in_interval)

expected_proportion = b - a
plt.figure(figsize=(10, 6))
plt.plot(n_values, results, marker='o', linestyle='--', label='Proportia masurata')

coefficients = np.polyfit(np.log(n_values), results, 1)
polynomial = np.poly1d(coefficients)
plt.plot(n_values, polynomial(np.log(n_values)), label='Dreapta de regresie', linestyle='-', color='g')

plt.axhline(expected_proportion, color='r', linestyle='--', label='Proportia teoretica')
plt.xlabel('Marimea eșantionului (n)')
plt.ylabel('Proportie')
plt.legend()
plt.title(f'Convergenta proportiei in intervalul ({a}, {b})')
plt.grid()
plt.show()
"""