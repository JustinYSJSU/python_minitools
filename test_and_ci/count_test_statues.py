def count_test_statues(results):
    result_dict = {}

    for test in results:
        if test['status'] in result_dict.keys():
            result_dict[test['status']] += 1
        else:
            result_dict[test['status']] = 1
    return result_dict

def main():
    results = [
    {"name": "motor_test", "status": "PASS"},
    {"name": "camera_test", "status": "FAIL"},
    {"name": "lidar_test", "status": "PASS"},
    {"name": "navigation_test", "status": "FAIL"},
    {"name": "imu_test", "status": "SKIP"},
    {"name": "battery_test", "status": "FAIL"},
    ]
    print(count_test_statues(results=results))

if __name__ == "__main__":
    main()