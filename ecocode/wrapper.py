"""Ecocode wrapper."""

import os
import json
from time import sleep
from functools import wraps
from multiprocessing import Process, Lock, Queue

import pandas as pd

from .additional_info import gather_machine_info
from .monitoring import monitor
from .process_machine import process_pc_info
from .send_data import send_data


def ecocode_decorator(
    country: str,
    name: str,
    api_key: str,
):
    """Ecocode Decorator."""
    def ecocode_wrapper(f):
        """Ecocode Wrapper."""
        @wraps(f)
        def ecocode_function(*args, **kwargs):
            """Ecocode Function."""
            def monitoring_function(lock: Lock, queue: Queue):
                """Monitoring function."""
                # Get the pid
                lock.acquire()
                pid = queue.get()
                lock.release()

                # Start the monitoring
                monitoring_information = []
                while True:
                    if queue.empty():
                        monitoring_information.append(
                            monitor(pid)
                        )
                    else:
                        break

                monit_df = pd.concat(
                    monitoring_information,
                    ignore_index=True
                )
                all_data = {}
                all_data['monitoring'] = monit_df.to_dict("records")
                all_data['machine'] = process_pc_info(
                    gather_machine_info()
                )
                all_data['country'] = country
                all_data['name'] = name
                all_data['api_key'] = api_key

                send_data(all_data)

            def running_function(lock: Lock, queue: Queue):
                """Running function."""
                # Get the current PID and send it to the monitoring
                print("PID", os.getpid())
                print('Parent PID', os.getppid())
                pid = os.getpid()
                queue.put(pid)

                # Wait for the monitoring to acknowledge
                lock.acquire()
                result = f(*args, **kwargs)
                queue.put('DONE !')

                return result

            lock = Lock()
            queue = Queue()

            # Create the monitoring process
            monitoring_process = Process(
                target=monitoring_function,
                name="Monitoring",
                args=(lock, queue)
            )
            monitoring_process.start()

            # Running process
            running_process = Process(
                target=running_function,
                name="Running Function",
                args=(lock, queue)
            )
            running_process.start()

            monitoring_process.join()
            running_process.join()

        return ecocode_function
    return ecocode_wrapper


@ecocode_decorator(country="FR")
def test_function(message: str, duration: int = 2):
    """Test function."""
    print('Entering the test function: ', message)
    print('time: ', duration, "s")
    sleep(duration)
    print('Ending the test function')
    return message


if __name__ == "__main__":
    test_function("Hello !", 10)
