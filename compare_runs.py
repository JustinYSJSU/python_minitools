"""Problem

A CI pipeline produces a JSON summary for every test run. When a new run has failures, engineers need to quickly determine:

Which tests are newly failing?
Which failures were already present?
Which previously failing tests are now passing?

Build a small CLI utility that compares two test-run result files.

Description

Create a script that can be run as:

python compare_runs.py <previous_run.json> <current_run.json>

The script should compare the test results from the two runs and print a concise summary.

Input / Example

previous_run.json

{
    "run_id": "1842",
    "tests": {
        "test_camera_init": "PASS",
        "test_lidar_connection": "PASS",
        "test_arm_home": "FAIL",
        "test_gripper_open": "FAIL",
        "test_robot_shutdown": "PASS"
    }
}

current_run.json

{
    "run_id": "1843",
    "tests": {
        "test_camera_init": "PASS",
        "test_lidar_connection": "FAIL",
        "test_arm_home": "FAIL",
        "test_gripper_open": "PASS",
        "test_robot_shutdown": "PASS",
        "test_battery_status": "FAIL"
    }
}
"""

import sys
import json
from pathlib import Path

# shoud be argparse here, done for simplicity
previous_run = sys.argv[1]
current_run = sys.argv[2]

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

def compare_run_dict(previous_run_dict, current_run_dict):
    run_key = {
        "prev": previous_run_dict['run_id'],
        "current": current_run_dict['run_id']
    }
    new_tests = [test for test in current_run_dict['tests'].keys() - previous_run_dict['tests'].keys()]

    still_failing = [test for test in current_run_dict['tests'].keys() & previous_run_dict['tests'].keys()
     if current_run_dict['tests'][test] == "FAIL" and previous_run_dict['tests'][test] == "FAIL"]
    
    new_failures = [test for test in current_run_dict['tests'].keys() | previous_run_dict['tests'].keys()
     if (current_run_dict['tests'][test] == "FAIL" and previous_run_dict['tests'].get(test) != "FAIL")]

    fixed = [test for test in current_run_dict['tests'].keys() & previous_run_dict['tests'].keys()
    if current_run_dict['tests'][test] == "PASS" and previous_run_dict['tests'][test] == "FAIL"]

    return(
        {
            "run_keys": run_key,
            "new_tests": new_tests,
            "still_failing": still_failing,
            "new_failures": new_failures,
            "fixed": fixed
        }
    )

def display_diff_outit(diff_result):
    print(f"Comparing Run {diff_result['run_keys']['prev']} -> {diff_result['run_keys']['current']} \n")
    print(f"New Failures: \n")
    for failure in diff_result['new_failures']:
        print(failure)

    print("\n")

    print(f"Still failing: \n")
    for failure in diff_result['still_failing']:
            print(failure)

    print("\n")

    print(f"Fixed: \n")
    for test in diff_result['fixed']:
        print(test)

    print("\n")

    print(f"New Tests: \n")
    for test in diff_result['new_tests']:
        print(test)

    print(f"Summary: \n New Failures: {len(diff_result['new_failures'])} \n Still Failing: {len(diff_result['still_failing'])} \n Fixed: {len(diff_result['fixed'])} \n New Tests: {len(diff_result['new_tests'])}")
def main():
    validate_json_file(previous_run)
    validate_json_file(current_run)

    previous_run_dict = load_json_to_dict(previous_run)
    current_run_dict = load_json_to_dict(current_run)

    diff_result = compare_run_dict(previous_run_dict, current_run_dict)

    display_diff_outit(diff_result)
    
if __name__ == "__main__":
    main()