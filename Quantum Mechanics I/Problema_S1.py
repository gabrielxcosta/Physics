import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import use
from scipy.integrate import quad

class WaveFunction:
    """
    Class representing a wave function of the form Psi(x) = exp(-alpha * x ** 2).

    Args:
        alpha (float): The value of the constant alpha.

    Attributes:
        alpha (float): The value of the constant alpha.

    """
    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, x):
        """
        Calculates the value of the wave function at a given point x.

        Args:
            x (float): The value of x.

        Returns:
            float: The value of the wave function at x.
        """
        return np.exp(-self.alpha * x ** 2)
        
    def normalization_constant(self):
        """
        Calculates the normalization constant for the wave function.

        Returns:
            float: The normalization constant.
        """
        integrand = lambda x: np.abs(self.__call__(x)) ** 2
        integral, _ = quad(integrand, -np.inf, np.inf)
        return 1 / np.sqrt(integral)
    
    def prob_density(self, x_start, x_end):
        """
        Calculates the probability of finding the particle in the range [x_start, x_end].

        Args:
            x_start (float): The lower bound of the measurement range.
            x_end (float): The upper bound of the measurement range.

        Returns:
            float: The probability of measuring the particle in the range [x_start, x_end].
        """
        integrand = lambda x: np.abs(self.normalization_constant() * self.__call__(x)) ** 2
        integral, _ = quad(integrand, x_start, x_end)

        return integral
    
    def plot_prob_density(self, x_min, x_max):
        """
        Plots the probability density of the wave function over the range [x_min, x_max].

        Args:
            x_min (float): The lower bound of the range to plot.
            x_max (float): The upper bound of the range to plot.
        """
        use("pgf")

        x_vals = np.linspace(x_min, x_max, 1000)
        y_vals = (self.normalization_constant() * self.__call__(x_vals)) ** 2
        fig = plt.figure(figsize=(20, 8), facecolor='w', dpi=400)
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(x_vals, y_vals, 'red', lw=3, alpha=.7, label=r"$|\Psi (x)|^{2}$")
        ax.figure.suptitle(fr"Probability density for $\alpha$ = {self.alpha}", fontsize=26)
        ax.set_title('Gaussian Integral', fontsize=22)
        ax.set_xlabel(r'$x$', fontsize=22)
        ax.set_ylabel(r'$| \Psi (x)|^{2}$', fontsize=22)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend(fontsize=18)
        legend.get_frame().set_alpha(.7)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        fig.savefig("ProbabilityDensity.png")
    
    def plot_prob_density_area(self, p, x_min, x_max, x_start, x_end):
        """
        Plots the probability density of the wave function over the range [x_min, x_max]
        and shades the area under the curve between [x_start, x_end].

        Args:
            x_min (float): The lower bound of the range to plot.
            x_max (float): The upper bound of the range to plot.
            x_start (float): The lower bound of the shaded area.
            x_end (float): The upper bound of the shaded area.
        """
        x_vals = np.linspace(x_min, x_max, 1000)
        y_vals = np.abs(self.normalization_constant() * self.__call__(x_vals)) ** 2

        fig = plt.figure(figsize=(20, 8), facecolor='w', dpi=400)
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(x_vals, y_vals, 'red', lw=3, alpha=.7, label=r"$|\Psi (x)|^{2}$")
        ax.fill_between(x_vals, y_vals, where=(x_vals >= x_start) & (x_vals <= x_end), alpha=.2, color='red')

        ax.figure.suptitle(fr"Probability density for $\alpha$ = {self.alpha}", fontsize=26)
        ax.set_title(fr'$p({x_start}, {x_end}) = {p:.3f} = {p * 100:.2f}$%', fontsize=22)
        ax.set_xlabel(r'$x$', fontsize=22)
        ax.set_ylabel(r'$| \Psi (x)|^{2}$', fontsize=22)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend(fontsize=18)
        legend.get_frame().set_alpha(.7)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        
        fig.savefig(f"ProbabilityDensityArea[{x_start}_{x_end}].png")

if __name__ == '__main__':
    start_time = time.time()

    alpha = 1.
    wf = WaveFunction(alpha)
    print('Normalization constant: ', wf.normalization_constant())

    a1, b1 = 0, 1
    a2, b2 = 1, 2
    a3, b3 = 0, 10

    p1 = wf.prob_density(a1, b1)
    wf.plot_prob_density_area(p1, -10, 10, a1, b1)
    p2 = wf.prob_density(a2, b2)
    wf.plot_prob_density_area(p2, -10, 10, a2, b2)
    p3 = wf.prob_density(a3, b3)
    wf.plot_prob_density_area(p3, -10, 10, a3, b3)

    print(f"Probability of finding the particle in the interval [{a1}, {b1}]: {p1:.3f}")
    print(f"Probability of finding the particle in the interval [{a2}, {b2}]: {p2:.3f}")
    print(f"Probability of finding the particle in the interval [{a3}, {b3}]: {p3:.3f}")

    wf.plot_prob_density(-10, 10)

    print("Elapsed time:", time.time() - start_time, "seconds")