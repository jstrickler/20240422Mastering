import sys

if len(sys.argv) < 2:
    print("please specify file(s) to count")
    sys.exit()

#  flag = sys.argv.pop(1)  # grab 1st argument

file_paths = sys.argv[1:]

for file_path in file_paths:
    with open(file_path) as file_in:
        line_count = 0
        for line in file_in:
            line_count += 1
    print(f"{file_path} has {line_count} lines")
