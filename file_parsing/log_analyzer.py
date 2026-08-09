import sys

def read_file():
    file_name = sys.argv[1]
    status_dict = {}
    msg_dict = {}
    line_counter = 0
    with open(file=file_name, mode="r", encoding='utf-8') as f:
        for line in f: # line split: [0] = date, [1] = time, [2] = status
            if not line.strip():
                continue
            line_counter = line_counter + 1
            split_line = line.split(sep=' ')
            status = split_line[2]
            msg_list = split_line[3: ]
            msg = " ".join(msg_list)

            if status == 'ERROR':
                msg_dict[msg] = msg_dict.get(msg, 0) + 1

            status_dict[status] = status_dict.get(status, 0) + 1
    sorted_msg_dict = dict(sorted(msg_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_msg_dict)
    print("Log Summary")
    print("-----------")
    print(f"Total Lines: {line_counter}")
    print("\n")

    for key in status_dict.keys():
        print(f"{key}: {status_dict[key]}\n")

    print("Top Errors")

    for key in sorted_msg_dict:
        print(f"{key}: {sorted_msg_dict[key]}")
    

def main():
    read_file()

if __name__ == '__main__':
    main()