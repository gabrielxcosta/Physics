import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('Accent_r')
sns.set_style('darkgrid')

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

ax = sns.lmplot(x='sin_ref_1', y='sin_inc', data=data)
ax.figure.set_dpi(1200)
ax.figure.set_size_inches(15, 12)
ax.figure.suptitle(r'Reta de Regressão - $\sin{ref_{1}}$ x $\sin{inc}$', fontsize=22, y=1.00)
ax.set_xlabels(r'$\sin{ref_{1}}$', fontsize=22)
ax.set_ylabels(r'$\sin{inc}$', fontsize=22)
plt.savefig('sin(ref_1)xsin(inc).png')

ax = sns.lmplot(x='sin_ref_2', y='sin_inc', data=data)
ax.figure.set_dpi(1200)
ax.figure.set_size_inches(15, 12)
ax.figure.suptitle(r'Reta de Regressão - $\sin{ref_{2}}$ x $\sin{inc}$', fontsize=22, y=1.00)
ax.set_xlabels(r'$\sin{ref_{2}}$', fontsize=22)
ax.set_ylabels(r'$\sin{inc}$', fontsize=22)
plt.savefig('sin(ref_2)xsin(inc).png')
