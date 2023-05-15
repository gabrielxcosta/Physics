import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt

start_time = time.time()

sns.set_palette('Accent_r')
sns.set_style('darkgrid')
plt.rc('mathtext', fontset='stix')
plt.rc('font', weight='bold')

# Constantes
G = 6.67430e-11   # m³/(kg s²)
R = 6.371e6       # m
M = 59742e24
rho0 = 13e3       # kg/m³ Núcleo
rho1 = 4500       # kg/m³ Manto Inferior

# Função g(r)
def g(r):
    if r <= 0.55*R:
        return (4/3) * np.pi * G * rho0 * r
    elif r <= R:
        return - (4/3) * np.pi * G * (rho1 * R**3) / r**2
    else:
        return 0

# Valores de r para plotagem
r_values = np.linspace(0, 1.1*R, 1000)

# Valores de g(r) para plotagem
g_values = np.array([np.abs(g(r)) for r in r_values])

# Define the colors for each region
colors = np.select( \
                [r_values <= 0.55*R, np.logical_and(r_values > 0.55*R, r_values <= R), r_values > R],
                ['green', 'blue', 'red']
                )

# Plotagem do gráfico
fig, ax = plt.subplots(figsize=(8, 6))
for i in range(1, len(r_values)):
    ax.step([r_values[i-1], r_values[i]], [g_values[i-1], g_values[i]], where='post', color=colors[i-1])
ax.set_xlabel(r'$r \ (m)$', fontsize=12, fontweight="bold")
ax.set_ylabel(r'$|g \ (r)| (m/s^{2})$', fontsize=12, fontweight="bold")
ax.set_title('Gráfico de ' + r"$|g(r)|$" + " em função de " + '$r$', fontsize=14, fontweight="bold", y=1.02)
plt.axvline(x=0.55*R, linestyle='--', color='blue')
plt.axvline(x=R, linestyle='--', color='red')
ax.fill_between(r_values, g_values, 0, where=r_values<=0.55*R, color='green', alpha=0.2)
ax.fill_between(r_values, g_values, 0, where=np.logical_and(r_values>0.55*R, r_values<=R), color='blue', alpha=0.2)
ax.fill_between(r_values, g_values, 0, where=r_values>R, color='red', alpha=0.2)

# Adiciona a legenda
leg = ax.legend(labels=['$\mathrm{Núcleo}$', '$\mathrm{Manto}$', '$\mathrm{Ext}$'],
                loc='upper right', fontsize=12, edgecolor='none', facecolor='white')

# Define as cores dos labels
leg.get_texts()[0].set_color('green')
leg.get_texts()[1].set_color('blue')
leg.get_texts()[2].set_color('red')
leg.get_lines()[0].set_color('green')
leg.get_lines()[1].set_color('blue')
leg.get_lines()[2].set_color('red')

leg.set_title('Camadas', prop={'size': 10, 'weight': 'bold'})

plt.tight_layout()

plt.savefig('|g(r)|_r.pdf')

print("--- %s seconds ---" % (time.time() - start_time))