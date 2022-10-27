import os
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Sender.config import sensor_value_count
from compute_statistics import calculate_statistics


def print_stats(data, writer=print):
    writer("\n".join(calculate_statistics(data)))

def convert_to_json(data):
    try:
        return None, json.loads(data)
    except:
        return ValueError("Invalid JSON format"), None

def input_collector(input_count):
    data = []
    for _ in range(input_count):
        datum = input().strip()
        if len(datum)>0:
            err, json_value = convert_to_json(datum)
            if err:
                raise err
            data.append(json_value)
    return data

if __name__ == "__main__":
    data = input_collector(sensor_value_count)
    print(f"Data From Sender..")
    print(data)
    
    print()
    print(f"Data From Receiver..")
    print_stats(data)
