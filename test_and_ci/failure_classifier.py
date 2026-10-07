def classify_failures(failures):
    """Given a list of dict CI failure descriptions, 
    cateorize each by type of failures

    Args: failures (list): list of all failed CI tests

    Returns: dict containing total tests, and categories of failures
    """
    res = {"categories": {}}
    res["total"] = len(failures)

    for test in failures:
        if test["status"] not in res:
            res[test["status"]] = 1
        else:
            res[test["status"]] += 1
        
        if test["status"] == "failed":
            message = test["message"].lower()
            if "timeout" in message:
                res["categories"]["timeout"] = res["categories"].get("timeout", 0) + 1
            elif "assert" in message:
                res["categories"]["assertion"] = res["categories"].get("assertion", 0) + 1
            elif "import" in message or "module" in message:
                res["categories"]["import"] = res["categories"].get("import", 0) + 1
            else:
                res["categories"]["unknown"] = res["categories"].get("unknown", 0) + 1
    return res

def main():
    failures = [
        {"test": "test_a", "status": "failed", "duration": 1.2,
        "message": "Connection TIMEOUT"},
        {"test": "test_b", "status": "failed", "duration": 0.4,
        "message": "AssertionError: expected 4, got 3"},
        {"test": "test_c", "status": "passed", "duration": 0.2,
        "message": ""},
        {"test": "test_d", "status": "failed", "duration": 0.1,
        "message": "No module named foo"},
    ]
    print(classify_failures(failures=failures))

if __name__ == "__main__":
    main()