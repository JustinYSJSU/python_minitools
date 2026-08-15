import sys
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(prog='select tests', description='select test from .json', epilog='n/a')
parser.add_argument("file_name")
parser.add_argument("--component", required=False)
parser.add_argument("--priority", required=False)
parser.add_argument("--include-disabled", action='store_true') # if provided => true | if not provided => false
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

def filter_tests(dict, test_component, test_priority, include_disabled):
    print(0)

def main():
    file_name = args.file_name
    test_component = args.component
    test_priority = args.priority
    include_disabled = args.include_disabled
    validate_json_file(file_name)
    valid_dict = load_json_to_dict(file_name=file_name)
    filter_tests(dict=valid_dict, test_component=test_component, test_priority=test_priority, include_disabled=include_disabled)

if __name__ == "__main__":
    main()