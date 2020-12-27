"""Example of a matrix multiplication function."""

import numpy as np

from ecocode import ecocode_decorator


@ecocode_decorator(country="FR", name="Matrix Multiplication", api_key="")
def function(n: int = 5000):
    """Matrix multiplication function."""
    A = np.random.random((n, n))
    B = np.random.random((n, n))
    C = A @ B
    D = np.random.random((n, n))
    E = C @ D
    return E


if __name__ == "__main__":
    function()
