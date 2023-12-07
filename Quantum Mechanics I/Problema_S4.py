import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import use
from scipy.integrate import quad

class InfiniteSquarePotentialWell:
    """
    Class representing a wave function of the form Psi(x) = sqrt(2/a) * sin(pi * x / a).

    Args:
        a (float): The width of the potential well.

    Attributes:
        a (float): The width of the potential well.

    """
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def __call__(self, x):
        """
        Calculates the value of the wave function at a given point x.

        Args:
            x (float): The value of x.

        Returns:
            float: The value of the wave function at x.
        """
        return np.sqrt(1 / self.a) * np.sin(self.n * np.pi * x / (2 * self.a))
        
    def normalization_constant(self):
        """
        Calculates the normalization constant for the wave function.

        Returns:
            float: The normalization constant.
        """
        integrand = lambda x: np.abs(self.__call__(x)) ** 2
        integral, _ = quad(integrand, 0, self.a)
        return 2 / np.sqrt(integral)
    
    def normalization_constant(self):
        """
        Calculates the normalization constant for the wave function.

        Returns:
            float: The normalization constant.
        """
        integrand = lambda x: np.abs(self.__call__(x)) ** 2
        integral, _ = quad(integrand, 0, self.a)
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
        fig = plt.figure(figsize=(8, 6), facecolor='w')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(x_vals, y_vals, 'red', lw=3, alpha=.7, label=r"$|\psi (x)|^{2}$")
        ax.figure.suptitle(fr"Probability density for $2a = {self.a:.3f}$", fontsize=24)
        ax.set_title('Infinite square potential well', fontsize=18)
        ax.set_xlabel(r'$x$', fontsize=22)
        ax.set_ylabel(r'$| \Psi (x)|^{2}$', fontsize=22)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend(fontsize=18)
        legend.get_frame().set_alpha(.7)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        fig.savefig("ProbabilityDensity.pdf")
    
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

        fig = plt.figure(figsize=(8, 6), facecolor='w')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(x_vals, y_vals, 'red', lw=3, alpha=.7, label=r"$|\Psi (x)|^{2}$")
        ax.fill_between(x_vals, y_vals, where=(x_vals >= x_start) & (x_vals <= x_end), alpha=.2, color='red')

        ax.figure.suptitle(fr"Probability density for $a = {self.a:.3f}$", fontsize=24)
        ax.set_title(fr'$p({x_start}, {x_end:.3f}) = {p:.3f} = {p * 100:.2f}$%', fontsize=18)
        ax.set_xlabel(r'$x$', fontsize=22)
        ax.set_ylabel(r'$| \Psi (x)|^{2}$', fontsize=22)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend(fontsize=18)
        legend.get_frame().set_alpha(.7)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        
        fig.savefig(f"ProbabilityDensityArea[{x_start}_{x_end}].pdf")

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

        fig = plt.figure(figsize=(8, 6), facecolor='w')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(x_vals, y_vals, 'red', lw=3, alpha=.7, label=r"$|\Psi (x)|^{2}$")
        ax.fill_between(x_vals, y_vals, where=(x_vals >= x_start) & (x_vals <= x_end), alpha=.2, color='red')

        # Infinite Square Potential Well box
        ax.hlines(0, x_start, x_end, colors='black', linewidth=2)
        ax.vlines(x_start, 0, np.max(y_vals), colors='black', linewidth=2)
        ax.vlines(x_end, 0, np.max(y_vals), colors='black', linewidth=2)

        # Add infinity symbol
        ax.text(x_start, np.max(y_vals), r'$\infty$', va='center', ha='right', fontsize=18)
        ax.text(x_end, np.max(y_vals), r'$\infty$', va='center', ha='left', fontsize=18)

        ax.figure.suptitle(fr"Probability density for $a = {self.a:.3f}$", fontsize=24)
        ax.set_title(fr'$p({x_start}, {x_end:.3f}) = {p:.3f} = {p * 100:.2f}$%', fontsize=18)
        ax.set_xlabel(r'$x$', fontsize=22)
        ax.set_ylabel(r'$| \Psi (x)|^{2}$', fontsize=22)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend(fontsize=18)
        legend.get_frame().set_alpha(.7)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        
        fig.savefig(f"ProbabilityDensityArea[{x_start}_{x_end}].pdf")


if __name__ == '__main__':
    start_time = time.time()

    a = np.pi
    wf = InfiniteSquarePotentialWell(a, 1)
    print('Normalization constant: ', wf.normalization_constant())

    x1, x2 = 0, 2 * a

    p1 = wf.prob_density(x1, x2)
    wf.plot_prob_density_area(p1, -.25, 2 * 6.4, x1, x2)

    print(f"Probability of finding the particle in the interval [{x1}, {x2}]: {p1:.3f}")

    wf.plot_prob_density(-.25, 2 * 6.4)
    
    print("Elapsed time:", time.time() - start_time, "seconds")