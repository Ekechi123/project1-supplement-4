def next_ten_numbers(start):
    return ",".join(str(start + i) for i in range(1, 11))


def list_to_comma_string(string_list):
    return ",".join(string_list)


def write_to_csv(filename, headers, data):
    with open(filename, 'w') as file:
        file.write(headers + "\n")
        file.write(data + "\n")

