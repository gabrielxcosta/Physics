import random
import progressbar
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class MonteCarlo:
    """
    Base class for estimating the value of pi using the Monte Carlo method.

    Methods:
    - monte_carlo(num_samples): Estimate the value of pi using the Monte Carlo method.
    """

    def monte_carlo(self, num_samples):
        """
        Estimate the value of pi using the Monte Carlo method.

        Parameters:
        - num_samples (int): The number of random darts to throw.

        Returns:
        float: An estimate of the value of pi based on the number of darts that land within a unit circle.
        """
        darts_in_circle = sum(1 for _ in range(num_samples) if random.uniform(0, 1) ** 2 + random.uniform(0, 1) ** 2 <= 1)
        estimate = 4 * darts_in_circle / num_samples
        return estimate

class PiAnimation(MonteCarlo):
    """
    Class for animating the estimation of pi using the Monte Carlo method.

    Parameters:
    - num_frames (int): Number of frames (and samples) to display in the animation.

    Methods:
    - update(frame): Update the animation frame.
    - run_animation(): Run the Monte Carlo simulation animation.
    """

    def __init__(self, num_frames=10):
        super().__init__()  # Call the constructor of the base class
        self.num_frames = num_frames
        self.colors = sns.color_palette('hls', n_colors=2)

    def generate_random_points(self, num_samples):
        """
        Generate random points within the unit square.

        Parameters:
        - num_samples (int): The number of random points to generate.

        Returns:
        list: List of (x, y) coordinates representing random points.
        """
        return [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_samples)]

    def plot_points(self, points, color, label, size):
        """
        Plot points on the graph.

        Parameters:
        - points (list): List of (x, y) coordinates representing points.
        - color (str): Color of the points.
        - label (str): Label for the legend.
        - size (int): Size of the points.
        """
        plt.scatter(*zip(*points), color=color, label=label, s=size)

    def update(self, frame):
        plt.cla()
        num_samples = 1000 * (frame + 1)

        # Generate random points
        points = self.generate_random_points(num_samples)

        # Separate points inside and outside the circle
        inside_circle = [(x, y) for x, y in points if x ** 2 + y ** 2 <= 1]
        outside_circle = [(x, y) for x, y in points if x ** 2 + y ** 2 > 1]

        # Plot the entire circle
        circle = plt.Circle((0, 0), 1, color='black', fill=False)
        plt.gca().add_patch(circle)

        # Plot the points with smaller size
        self.plot_points(inside_circle, self.colors[0], 'Inside Circle', 20)
        self.plot_points(outside_circle, self.colors[1], 'Outside Circle', 20)

        # Display the estimate of pi and number of samples
        estimate = self.monte_carlo(num_samples)
        plt.suptitle(fr'Monte Carlo Methods', fontsize=18, y=.95)
        plt.title(fr'Estimation of $\pi$: {estimate:.5f} | $N$: {num_samples}', fontsize=14)

        # Set figure size to be square
        plt.gcf().set_size_inches(8, 8)

        # Set axis limits
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        # Add legend inside the plot (upper-left corner)
        plt.legend(loc='upper left', fontsize=15)

    def run_animation(self):
        print("Rendering animation...\n")
        animation = FuncAnimation(plt.gcf(), self.update, frames=self.num_frames, repeat=False)
        fig_outfile = f"MonteCarlo_Pi.gif"

        bar = progressbar.ProgressBar(maxval=100).start()

        try:
            # Save the animation with progress callback
            animation.save(
                fig_outfile,
                fps=6000 / 30,
                dpi=300,
                progress_callback=lambda i, n: bar.update(i + 1)  # Note the i + 1 adjustment,
            )
        finally:
            bar.finish()
        print(f"\nFigure saved as {fig_outfile}")

        # Example usage:
# Create an instance of the PiAnimation class with the desired number of frames (samples)
pi_animation = PiAnimation(num_frames=30)

# Run the animation
pi_animation.run_animation()