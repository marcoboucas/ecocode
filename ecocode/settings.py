"""Settings file."""


class settings:
    """Settings class."""

    COLUMNS = [
        'PID', "USER", "PR", "NI", "VIRT",
        "RES", "SHR", "S", "CPU", "MEM", "TIME",
        "COMMAND"
    ]

    SERVER_URL = "http://localhost:5000/addRun"
