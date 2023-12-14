import torch
import time

def madelung_constant(N):
    """
    Calculate the Madelung constant for a 2D lattice of charges.

    The Madelung constant represents the electrostatic potential energy of an
    ionically bonded crystal in two dimensions. It is calculated as the sum of
    the contributions from all charges in the lattice.

    Parameters:
    N (int): The maximum distance from the central charge in the lattice.

    Returns:
    float: The calculated Madelung constant.

    This function calculates the Madelung constant for a square lattice of
    charges with charges alternately positive and negative at integer grid
    points in a 2D plane. The function uses a summation technique to determine
    the potential energy contribution from each charge in the lattice within
    a specified range.
    """
    i, j = torch.meshgrid(
        torch.arange(-N, N + 1), 
        torch.arange(-N, N + 1), 
        indexing='ij'
    )
    mask = (i != 0) | (j != 0)
    i, j = i[mask], j[mask]
    alpha = (torch.pow(-1, i + j) / torch.sqrt(i ** 2 + j **2).float()).sum()
    return abs(alpha)

N = 22500
start_time = time.time()
result = madelung_constant(N)
print("Madelung Constant for a", N, "x", N, "grid:", result.item())
print("Elapsed Time:", time.time() - start_time, " seconds......")