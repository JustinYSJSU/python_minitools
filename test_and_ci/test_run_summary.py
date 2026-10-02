import sys

def count_test_statues(results, res):
    """Helper function to count test statues

    Args: results (list): List of objects containing test results
          res (dict): res dict to append results to

    Returns: edited res dict containing all categories / values for statues
    """

    for test in results:
        if test["status"] not in res:
            res[test["status"]] = 1
        else:
            res[test["status"]] += 1
    res["pass_rate"] = res["passed"] / res["total"]
    return res

def calculate_durations(results, res):
    """Helper function to calcuate total test duration and slowest test

    Args: results (list): List of objects containing test results
          res (dict): res dict to append results to

    Returns: edited res dict containing total duration
    """
    total = 0.0
    slowest_time = sys.float_info.min
    slowest_name = ""
    for test in results:
        if test["duration"] > slowest_time:
            slowest_time = test["duration"]
            slowest_name = test["name"]
        total += test["duration"]
    res["total_duration"] = total
    res["slowest_test"] = slowest_name
    return res

def summarize_test_run(results):
    """Summarize a given test run given its results

    Args: results (list): List of objects containing test results

    Returns: dict containing all categories / values for results
    """
    res = {}
    res["total"] = len(results) 
    count_test_statues(results=results, res=res)
    calculate_durations(results=results, res=res)

    res["ci_status"] = ""
    if "failed" in res:
        res["ci_status"] = "failed"
    else:
        res["ci_status"] = "passed"
    return res

def main():
    results = [
        {"name": "test_login", "status": "passed", "duration": 0.42},
        {"name": "test_logout", "status": "passed", "duration": 0.18},
        {"name": "test_payment", "status": "failed", "duration": 1.73},
        {"name": "test_search", "status": "skipped", "duration": 0.01},
        {"name": "test_profile", "status": "failed", "duration": 0.91},
    ]

    if len(results) == 0:
        print("Empty results list")
        sys.exit(1)
    print(summarize_test_run(results=results))

if __name__ == "__main__":
    main()