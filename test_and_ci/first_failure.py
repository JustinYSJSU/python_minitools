def first_failed_test(results):
    """Given a list of test results,
    return the first test that failed
    """
    for test in results:
        if test['status'] == 'FAIL':
            return test['name']
    return None

def main():
    results = [
    {"name": "motor_test", "status": "PASS"},
    {"name": "encoder_test", "status": "PASS"},
    {"name": "camera_test", "status": "FAIL"},
    {"name": "lidar_test", "status": "FAIL"},
    {"name": "navigation_test", "status": "PASS"},
    ]
    print(first_failed_test(results=results))

if __name__ == '__main__':
    main()