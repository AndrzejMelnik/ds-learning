import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n = 1000
mi = 50
sigma = 10

np.random.seed(42)
samples = np.random.normal(loc=mi, scale=sigma, size=n)
print(samples)

subset = sum(((samples <= 60) & (samples >= 40)))
print(subset)

x = (subset / n) * 100
y = 68.27

diff = (x - y)


plt.hist(samples, bins=30, density=True, alpha=0.6, label='Próbki')

# Krzywa teoretycznego rozkładu normalnego
xmin, xmax = plt.xlim()
x_vals = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x_vals, mi, sigma)
plt.plot(x_vals, p, 'r', linewidth=2, label='Rozkład normalny')

# Zaznaczenie przedziału 40–60
plt.axvline(40, color='green', linestyle='--', label='Granice 1σ')
plt.axvline(60, color='green', linestyle='--')

# Tytuł i opisy
plt.title(f'Histogram próbek N({mi}, {sigma})\n'
          f'W przedziale [40,60]: {x:.2f}% (teoria: {y}%)')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')
plt.legend()

plt.show()
