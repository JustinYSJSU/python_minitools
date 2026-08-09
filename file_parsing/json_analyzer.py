import json
import sys

LOW_BATTERY = 20.0
def load_file():
    file_name = sys.argv[1]
    file_data = ""
    with open(file_name, 'r', encoding='utf-8') as file:
        file_data= json.load(file)
    return file_data

def count_robots(file_data):
    robot_total_count = len(file_data)
    robot_online_count = len([robot for robot in file_data if robot['online']])
    robot_offline_count = robot_total_count - robot_online_count
    return(
        {
            "total_count": robot_total_count,
            "online_count": robot_online_count,
            "offline_count": robot_offline_count
        }
    )

def calculate_battery(file_data):
    battery_total = 0.0
    low_battery = []
    for robot in file_data:
        if robot['online']:
            battery_total += robot['battery']
            if robot['battery'] < LOW_BATTERY:
                low_battery.append(robot)
    return(
        {
            "low_battery": low_battery,
            "avg_battery": battery_total / len([robot for robot in file_data if robot['online']])
        }
    )

def calculate_cpu(file_data):
    cpu_total = 0.0
    cpu_max = {
        "cpu": 0.0,
        "robot": ''
    }
    for robot in file_data:
        if robot['online']:
            cpu_total += robot['cpu']
            max_temp = max(cpu_max['cpu'], robot['cpu'])
            if max_temp >= cpu_max['cpu']:
                cpu_max['cpu'] = robot['cpu']
                cpu_max['robot'] = robot['robot_id']
    return(
        {
            "max_cpu": cpu_max,
            "avg_cpu": cpu_total / len([robot for robot in file_data if robot['online']])
        }
    )

def display_data(robot_counts, battery_metrics, cpu_metrics):
    print("Robot Health Report")
    print("-------------------")
    print("\n")

    print(f"Total Robots: {robot_counts['total_count']}")
    print(f"Online: {robot_counts['online_count']}")
    print(f"Offline: {robot_counts['offline_count']}")
    print("\n")

    print(f"Average Battery: {battery_metrics['avg_battery']}")
    print(f"Average CPU: {cpu_metrics['avg_cpu']}")
    print("\n")

    print("Low Battery Robots (<20%)")
    for robot in battery_metrics['low_battery']:
        print(f"{robot['robot_id']} ({robot['battery']})")
    print("Highest CPU Robot")
    print(f"{cpu_metrics['max_cpu']['robot']} ({cpu_metrics['max_cpu']['cpu']})")

def main():
    file_data = load_file()
    robot_counts = count_robots(file_data=file_data)
    battery_metrics = calculate_battery(file_data=file_data)
    cpu_metrics= calculate_cpu(file_data=file_data)
    display_data(robot_counts=robot_counts, battery_metrics=battery_metrics, cpu_metrics=cpu_metrics)

if __name__ == '__main__':
    main()