import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='darkgrid', context='notebook')

class ExplicitEuler:
    def __init__(self, ode, h, t_range, s0):
        """
        Initializes the parameters for the explicit Euler method.

        Parameters:
        ode (function): The ODE function f(t, s).
        h (float): Step size.
        t_range (tuple): Time range (t_start, t_end).
        s0 (float): Initial condition for s.
        """
        self.ode = ode
        self.h = h
        self.t_range = t_range
        self.s0 = s0
        self.t = np.arange(t_range[0], t_range[1] + h, h)  # Numerical grid
        self.s = np.zeros(len(self.t))  # Initialize the solution vector
        self.filename = f'SimpleODE_Euler_h_{h}'
    
    def solve(self):
        """
        Solves the ODE using the explicit Euler method.
        """
        self.s[0] = self.s0
        for i in range(len(self.t) - 1):
            self.s[i + 1] = self.s[i] + self.h * self.ode(self.t[i], self.s[i])
        return self.t, self.s

    def plot(self, exact_solution=None):
        """
        Plots the approximate solution and optionally the exact solution.

        Parameters:
        exact_solution (function): Exact solution for comparison (optional).
        """
        plt.figure(figsize=(12, 8))
        plt.plot(self.t, self.s, color='#c00000', label='Numerical Solution', linestyle='dashdot', lw=4)
        
        if exact_solution:
            plt.plot(self.t, exact_solution(self.t), color='#0070c0', label='Exact Solution', lw=2)
        
        plt.title('Numerical and Exact Solution for a Simple ODE', fontsize=14)
        plt.xlabel(r'$t$')
        plt.ylabel(r'$f(t)$')
        plt.legend(loc='lower right', facecolor='white')
        plt.savefig(self.filename + '.pdf')

if __name__ == "__main__":
    # Define parameters
    ode = lambda t, s: np.exp(-t)  # ODE
    h = 0.001  # Step size
    t_range = (0, 1)  # Time range
    s0 = -1  # Initial condition

    # Exact solution for comparison
    exact_solution = lambda t: -np.exp(-t)

    # Initialize and solve the ODE
    solver = ExplicitEuler(ode, h, t_range, s0)
    t, s = solver.solve()

    # Plot the results
    solver.plot(exact_solution=exact_solution)