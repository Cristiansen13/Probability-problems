import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp
import math as math

# Ex 3
"""
def simulate_poisson(lmbda, size):
    u = np.random.random(size)
    x = -np.log(u) / lmbda     
    poisson_data = np.floor(x).astype(int)
    return poisson_data

def simulate_binomial(n, p, size):
    binomial_data = np.zeros(size, dtype=int)
    for i in range(n):
        u = np.random.random(size)
        binomial_data += (u < p).astype(int)
    return binomial_data

def poisson_pmf(k, lmbda):
    return (lmbda ** k) * exp(-lmbda) / factorial(k)

def plot_histogram(data, title, xlabel, ylabel, pmf_theoretical=None):
    plt.hist(data, bins=range(max(data) + 1), align='left', density=True, rwidth=0.8, alpha=0.5, label='Observată')
    if pmf_theoretical is not None:
        plt.plot(range(max(data) + 1), pmf_theoretical, 'ro-', label='Teoretică')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

n = 20
lmbda = 1
size = 10000

poisson_data = simulate_poisson(lmbda, size)
pmf_poisson = [poisson_pmf(k, lmbda) for k in range(max(poisson_data) + 1)]
plot_histogram(poisson_data, 'Histograma Poisson', 'Valori', 'Probabilitate', pmf_theoretical=pmf_poisson)

p_binomial = lmbda / n
binomial_data = simulate_binomial(n, p_binomial, size)
pmf_binomial = [poisson_pmf(k, lmbda) for k in range(max(binomial_data) + 1)]
plot_histogram(binomial_data, 'Histograma Binomială', 'Valori', 'Probabilitate', pmf_theoretical=pmf_binomial)

plt.hist(poisson_data, bins=range(max(poisson_data) + 1), align='left', density=True, rwidth=0.4, alpha=0.5, label='Poisson')
plt.hist(binomial_data, bins=range(max(binomial_data) + 1), align='left', density=True, rwidth=0.4, alpha=0.5, label='Binomial')
plt.title('Comparare Histogramelor')
plt.xlabel('Valori')
plt.ylabel('Probabilitate')
plt.legend()
plt.show()
"""

# Ex 4
"""
def hypergeom_pmf(k, N, K, n):
    return (math.comb(K, k) * math.comb(N - K, n - k)) / math.comb(N, n)

def simulate_hypergeometric(N, K, n, size):
    population = np.arange(N)
    success_population = np.arange(K)
    hypergeo_data = np.zeros(size, dtype=int)

    for i in range(size):
        sample = np.random.choice(population, n, replace=False)
        hypergeo_data[i] = np.sum(np.isin(sample, success_population))

    return hypergeo_data

def plot_histogram(data, title, xlabel, ylabel, pmf_theoretical=None):
    plt.hist(data, bins=range(max(data) + 1), align='left', density=True, rwidth=0.8, alpha=0.5, label='Observată')
    if pmf_theoretical is not None:
        plt.plot(range(max(data) + 1), pmf_theoretical, 'ro-', label='Teoretică')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

N = 100
K = 20
n = 20
size = 1000

hypergeo_data = simulate_hypergeometric(N, K, n, size)
pmf_hypergeo = [hypergeom_pmf(k, N, K, n) for k in range(max(hypergeo_data) + 1)]
plot_histogram(hypergeo_data, 'Histograma Hipergeometrică', 'Valori', 'Probabilitate', pmf_theoretical=pmf_hypergeo)
"""