"""Example of a matrix multiplication function."""

import numpy as np

from ecocode import ecocode_decorator


@ecocode_decorator(country="FR", name="Matrix Multiplication", api_key="")
def function(n: int = 10000):
    """Matrix multiplication function."""
    A = np.random.random((n, n))
    B = np.random.random((n, n))
    C = A @ B
    return C


if __name__ == "__main__":
    function()
