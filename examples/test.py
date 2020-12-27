"""Example of empty function."""

from time import sleep

from ecocode import ecocode_decorator


@ecocode_decorator(
    country="FR",
    name="Test function",
    api_key=""
)
def function():
    """Sleep."""
    sleep(2)
    return False


if __name__ == "__main__":
    function()
