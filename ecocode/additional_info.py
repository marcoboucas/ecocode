"""Gather additional information about the machine."""

import subprocess


def gather_machine_info():
    """Gather information about the current machine."""
    # Gather information about the cpu
    cpu_info = subprocess.run("lscpu", capture_output=True).stdout.decode()

    # Gather RAM info
    ram_info = subprocess.run("free", capture_output=True).stdout.decode()

    return {
        "cpu": cpu_info,
        "ram": ram_info
    }


if __name__ == "__main__":
    import json
    with open('./machine_info.json', "w") as _:
        json.dump(gather_machine_info(), _, indent=2)
