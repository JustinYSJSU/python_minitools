import argparse
import sys
import json
from pathlib import Path

parser = argparse.ArgumentParser(prog='json to txt', description='convert .json results to .txt', epilog='n/a')
parser.add_argument("file_name")
parser.add_argument("--output", required=False)
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
    print()

if __name__ == "__main__":
    main()