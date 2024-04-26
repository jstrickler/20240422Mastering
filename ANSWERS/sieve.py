import sys

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

limit = 10

flags = [True] * limit
print(f"{flags = }")

for num in range(2, limit):
    if flags[num]:  # num is prime     #  x == y   x  > y
        print(num, end=' ')
        for multiple_of_num in range(2 * num, limit, num):
            flags[multiple_of_num] = False
    print(f"{flags = }\n")
    
print()

