"""Process the machine information."""
import json
from typing import Dict, Any
import re


def process_cpu(cpu_info: str) -> Dict[str, Any]:
    """Process the CPU info."""
    data = {}
    for line in cpu_info.split('\n'):
        tokens = re.split(r": +", line)
        if len(tokens) == 2:
            data[tokens[0]] = tokens[1].strip()

    return data


def process_ram(ram_info: str) -> Dict[str, Any]:
    """Process the RAM info."""
    data = {}
    lines = ram_info.split('\n')
    # Get the total Mem (not swap)
    line = re.split(r" +", lines[1])
    data['total_ram'] = str(line[1])

    return data


def process_pc_info(raw_data):
    """Process the pc information."""
    return {
        "ram": process_ram(raw_data['ram']),
        "cpu": process_cpu(raw_data['cpu'])
    }


if __name__ == "__main__":
    with open('./machine_info.json', "r") as _:
        data = json.load(_)
    with open('./machine_info_processed.json', "w") as _:
        json.dump(
            process_pc_info(data),
            _, indent=2
        )
