import numpy as np
import matplotlib.pyplot as plt

def prob(n):
    cnt = 0
    for i in range(10000):
        sample = np.random.uniform(0, 1, size=n)
        for j in range(n):
            if sample[j] < 0.5:
                sample[j] = 0
            else:
                sample[j] = 1
        cnt1 = 0 
        for j in range(n):
            if sample[j] == 1:
                cnt1 += 1
            if sample[j] == 0:
                cnt1 = 0
            if cnt1 == 4:
                cnt += 1
                break
    P = cnt/10000
    return P
def rec(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1/16
    else:
        return 1/16 + 1/2 * rec(n - 1) + 1/4 * rec(n - 2) + 1/8 * rec(n - 3) + 1/16 * rec(n - 4)

n = 21
x_values = range(1, n)
prob_values = [prob(i) for i in x_values]
rec_values = [rec(i) for i in x_values]

plt.plot(x_values, prob_values, marker='o', linestyle='-', color='b', label='Prbabilitate teoretica')
plt.plot(x_values, rec_values, marker='s', linestyle='-', color='r', label='Probabilitate practica')

plt.xlabel('Numar de biti')
plt.ylabel('Probabilitate')
plt.title('Comparatie intre probabilitatea teoretica si practica')
plt.legend()
plt.show()