counts = {}  # create new empty dict

with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip()
        counts[breakfast_item] = counts.get(breakfast_item, 0) + 1   # if so, increment count for specified key

for item, count in counts.items():
    print(item, count)
