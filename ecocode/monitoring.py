"""Monitoring function."""

from typing import List
import subprocess

import pandas as pd
from .settings import settings


def monitor(
    pid: int,
    duration: float = 1,
    frequency: float = 30
):
    """Monitor processus."""
    command = [
        "top",
        "-b",
        "-d", str(1/frequency),
        "-n", str(int(duration * frequency)),
        "-p", str(pid)
    ]

    output = subprocess.run(
        command,
        capture_output=True
    ).stdout

    batches = split_batches(output)

    batches_info = list(map(process_batch, batches))

    batches_info_df = pd.DataFrame.from_records(batches_info)
    return batches_info_df


def split_batches(raw_text: str):
    """Split between different batches."""
    splits = raw_text.split(b'\n\n')
    batches = []
    for i in range(0, len(splits), 2):
        batches.append(splits[i:i+2])
    return batches


def process_batch(batch: List[str]):
    """Process one batch."""
    # Retrive general information

    # Retrieve information about all the processes
    process_info = []
    for line in batch[1].split(b'\n')[1:]:
        infos = line.split(b' ')
        infos = list(map(
            lambda x: x.decode(),
            filter(lambda x: len(x) > 0, infos)
        ))
        process_info.append(
            dict(zip(
                settings.COLUMNS,
                infos
            ))
        )

    return process_info[0]


if __name__ == "__main__":
    monitor(1)
