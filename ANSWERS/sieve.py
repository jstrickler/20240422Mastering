import sys

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * limit

for num in range(2, limit):
    if flags[num]:  # num is prime     #  x == y   x  > y
        print(num, end=' ')
        for multiple_of_num in range(2 * num, limit, num):
            flags[multiple_of_num] = False
print()

soup = "clam chowder"
if soup:
    print("Soup is goooood")
