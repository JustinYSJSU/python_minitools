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

def create_filter_dict(arg_dict):
    filter_dict = {}
    for key, value in arg_dict.items():
        if arg_dict[key] is not None:
            filter_dict[key] = value
    return filter_dict

def filter_tests(test_dict, filter_dict):
    final_tests = []
    filter_dict_keys_no_disable = [key for key in filter_dict if key != "include_disabled"]

    for test in test_dict['tests']:
        matches = True
        for key in filter_dict_keys_no_disable:
            if test[key] != filter_dict[key]:
                matches = False
                break
        if matches:
            if not test["enabled"] and not filter_dict["include_disabled"]:
                continue
            else:
                final_tests.append(test)
    return final_tests

def main():
    file_name = args.file_name
    arg_dict = {
        "component": args.component,
        "priority": args.priority,
        "include_disabled": args.include_disabled
    }
    filter_dict = create_filter_dict(arg_dict=arg_dict)
    validate_json_file(file_name)
    test_dict = load_json_to_dict(file_name=file_name)
    final_tests = filter_tests(test_dict=test_dict, filter_dict=filter_dict)

    print(f"Selected {len(final_tests)} tests")
    for test in final_tests:
        print(test['name'])

if __name__ == "__main__":
    main()