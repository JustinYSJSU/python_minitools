results = [
    {"name": "motor_test", "status": "PASS"},
    {"name": "camera_test", "status": "FAIL"},
    {"name": "lidar_test", "status": "PASS"},
    {"name": "navigation_test", "status": "FAIL"},
    {"name": "imu_test", "status": "PASS"},
]

def get_failed_tests(results):
    """Given a list of key/value pairs (tests + results),
    return the name of each test that failed
    """
    res = [test['name'] for test in results if test['status'] == 'FAIL']
    return res

def main():
    results = [
    {"name": "motor_test", "status": "PASS"},
    {"name": "camera_test", "status": "FAIL"},
    {"name": "lidar_test", "status": "PASS"},
    {"name": "navigation_test", "status": "FAIL"},
    {"name": "imu_test", "status": "PASS"},
    ]
    print(get_failed_tests(results=results))

if __name__ == '__main__':
    main()
