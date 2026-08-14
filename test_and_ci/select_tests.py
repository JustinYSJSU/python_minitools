import sys
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(prog='select tests', description='select test from .json', epilog='n/a')
parser.add_argument("file_name")
parser.add_argument("--component", required=False)
parser.add_argument("--priority", required=False)

args = parser.parse_args()

def validate_json_file(file_name):

    path_name = Path(file_name)
    if not path_name.is_file():
        print(f"{path_name} not found")
        sys.exit(1)
    if not path_name.suffix == '.json':
        print(f"{path_name} is not of type .json")
        sys.exit(1)

def load_json_to_dict(file_name):
    with open(Path(file_name), 'r') as f:
        data = json.load(f)
    return data

def main():
    file_name = args.file_name
    test_component = args.component
    test_priority = args.priority

    validate_json_file(file_name)
    valid_dict = load_json_to_dict(file_name, test_component=None, test_priority=None)
if __name__ == "__main__":
    main()