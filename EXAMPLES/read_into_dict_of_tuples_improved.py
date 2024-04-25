import sys
from pprint import pprint

def main():
    if len(sys.argv) < 2:
        print("please specify data file")
        sys.exit()

    file_path = sys.argv[1]

    knight_data = read_data(file_path)
    pretty_print(knight_data)
    print()
    print_titles(knight_data)
    print()
    info = get_knight_data(knight_data, 'Robin')
    print(f"{info = }")
    field = get_knight_attribute(knight_data, 'Robin', 2)
    print(f"{field = }")
    

def read_data(file_path):
    knight_info = {}  # create empty dict
    with open(file_path) as knights_in:
        for line in knights_in:
            name, title, color, quest, comment = line.rstrip('\n\r').split(":")
            knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value
    return knight_info

def pretty_print(info):
    pprint(info)

def print_titles(info):
    for name, data in info.items():
        print(data[0], name)

def get_knight_data(info, knight):
    return info[knight]

def get_knight_attribute(info, knight, attr_index):
    return info[knight][attr_index]

main()