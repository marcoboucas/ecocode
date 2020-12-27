"""Send the data to the server."""
import json
import requests
from .settings import settings


def send_data(data):
    """Send the data to the server."""

    try:

        requests.post(
            settings.SERVER_URL,
            json=data
        )
    except requests.exceptions.ConnectionError:
        print("Is the server running ? Data cannot be sent to the server")
        return False
    return True
