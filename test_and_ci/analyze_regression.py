def convert_list(run):
    """Helper function to convert each list of results to a singular
    result dict

    Args:
        run (list): The run to convert
    
    Returns a dictionary conversion of run
    """
    res = {}

    for test in run:
        res[test['name']] = test['status']
    return res

def analyze_regression(prev_run, current_run):
    """Compute new/fixed failures, and newly added
    tests from the previous run

    Args:
        prev_run: Previous run
        current_run: Current run

    Returns a dictionary containing results
    """
    res = {
        "new_failures": [],
        "fixed_failures": [], 
        "new_tests": []
    }

    res["new_failures"] = [test for test in current_run.keys() if test in prev_run and prev_run[test] == "PASS" and current_run[test] == "FAIL"]
    res["fixed_failures"] = [test for test in current_run.keys() if test in prev_run and prev_run[test] == "FAIL" and current_run[test] == "PASS"]
    res["new_tests"] = current_run.keys() - prev_run.keys()

    return res

def main():
    prev_run = [
        {"name": "motor_test", "status": "PASS"},
        {"name": "camera_test", "status": "FAIL"},
        {"name": "lidar_test", "status": "PASS"},
        {"name": "navigation_test", "status": "FAIL"},
        {"name": "imu_test", "status": "PASS"},
    ]

    current_run = [
        {"name": "motor_test", "status": "PASS"},
        {"name": "camera_test", "status": "PASS"},
        {"name": "lidar_test", "status": "FAIL"},
        {"name": "navigation_test", "status": "FAIL"},
        {"name": "battery_test", "status": "FAIL"},
    ]

    print(analyze_regression(prev_run=convert_list(prev_run), current_run=convert_list(current_run)))

if __name__ == "__main__":
    main()