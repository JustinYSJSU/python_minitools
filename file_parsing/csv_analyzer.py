import sys
import csv

def read_csv():
    file_name = sys.argv[1]
    line_counter = 0
    total_runtime = 0.0
    test_dict = {}
    with open(file=file_name, newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # automatically skip first line

        for line in reader: # iterate over reader, not csv_file
            line_counter += 1
            total_runtime += float(line[2])
            test_dict[line[0]] = {"status": line[1], "run_time": float(line[2])}
    pass_counter = len([test for test in test_dict.keys() if test_dict[test]["status"] == "PASS"])
    fail_counter = line_counter - pass_counter

    print("Test Summary")
    print("------------")
    print("\n")
    print(f"Total tests: {line_counter}")
    print("\n")

    print(f"PASS: {pass_counter}")
    print(f"FAIL: {fail_counter}")
    print(f"Pass Rate: {round((pass_counter/line_counter) * 100, 1)}")
    print("\n")
    slow_tests = list(dict(sorted(test_dict.items(), key=lambda item: item[1]["run_time"], reverse=True)).keys())
    print("Slowest Tests")
    print(f"{slow_tests[0]}: {test_dict[slow_tests[0]]["run_time"]}")
    print(f"{slow_tests[1]}: {test_dict[slow_tests[1]]["run_time"]}")
    print(f"{slow_tests[2]}: {test_dict[slow_tests[2]]["run_time"]}")

def main():
    read_csv()

if __name__ == '__main__':
    main()