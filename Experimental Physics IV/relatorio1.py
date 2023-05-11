import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

start_time = time.time()

sns.set_palette('Accent_r')
sns.set_style('darkgrid')
plt.rc('mathtext', fontset='stix')  # set fontset to STIX
plt.rc('font', weight='bold')

inc = np.array([x for x in range(0, 100, 10)])
ref1 = np.array([0, 6.5, 13, 19.5, 25.5, 31, 35.5, 39.5, 42, 90])
ref2 = np.array([0, 15, 31, 48, 73, 50, 60, 70, 80, 90])

data = pd.DataFrame(
    {
        'incidencia' : inc,
        'refracao_1' : ref1,
        'refracao_2' : ref2,
        'sin_inc' : np.array([np.sin(np.deg2rad(x)) for x in inc]),
        'sin_ref_1' : np.array([np.sin(np.deg2rad(x)) for x in ref1]),
        'sin_ref_2' : np.array([np.sin(np.deg2rad(x)) for x in ref2])
    }
)

data.to_csv('experimento_1_lei_de_snell.csv', sep=',')

# Correlation matrix
corr_matrix = data.corr()

# Create heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)
ax.set_title('Mapa de Calor - Investigação da Matriz de Correlações', fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig('heatmap_correlation_1.pdf')

# Plot 1
fig, ax = plt.subplots(figsize=(8, 6))
slope, intercept, r_value, p_value, std_err = stats.linregress(data.sin_ref_1, data.sin_inc)
sns.regplot(x='sin_ref_1', y='sin_inc', data=data, ax=ax)
ax.set_xlabel(r'$\sin{ref_{1}}$', fontsize=12, fontweight="bold")
ax.set_ylabel(r'$\sin{inc}$', fontsize=12, fontweight="bold")
ax.set_title(r'Reta de Regressão - $\sin{ref_{1}}$ x $\sin{inc}$' + fr' - $\alpha_{1} = {slope:.3f}$' + fr' - $R^{2} = {r_value ** 2:.3f}$', fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig('sin_ref_1_x_sin_inc.pdf')

# Plot 2
fig, ax = plt.subplots(figsize=(8, 6))
slope, intercept, r_value, p_value, std_err = stats.linregress(data.sin_ref_2, data.sin_inc)
sns.regplot(x='sin_ref_2', y='sin_inc', data=data, ax=ax)
ax.set_xlabel(r'$\sin{ref_{2}}$', fontsize=12, fontweight="bold")
ax.set_ylabel(r'$\sin{inc}$', fontsize=12, fontweight="bold")
ax.set_title(r'Reta de Regressão - $\sin{ref_{2}}$ x $\sin{inc}$' + fr' - $\alpha_{2} = {slope:.3f}$' + fr' - $R^{2} = {r_value ** 2:.3f}$', fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig('sin_ref_2_x_sin_inc.pdf')

print("--- %s seconds ---" % (time.time() - start_time))
