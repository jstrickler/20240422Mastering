import sys

if len(sys.argv) < 3:
    print("Please specify target letter and word file")
    sys.exit()

target = sys.argv[1].lower()
file_path = sys.argv[2]

count = 0
with open(file_path) as words_in:
    for raw_line in words_in:
        if raw_line.lower().startswith(target):
            count += 1
print(f"{count} words start with '{target}'")
