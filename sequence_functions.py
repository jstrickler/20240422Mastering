colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

print(f"{len(colors) = }")
print(f"{min(colors) = }")
print(f"{max(colors) = }")
print(f"{sorted(colors) = }")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]
print(f"{sorted(nums) = }")
print(f"{sum(nums) = }")

rcolors = reversed(colors)  # rcolors is an iterator
print(f"{rcolors = }")
for color in rcolors:
    print(color)
print()

a = ['a', 'b', 'c']
b = [10, 20, 30]
z = zip(a, b)
print(f"{z = }")
for x in z:
    print(x)
print()
print(f"{list(zip(a, b)) = }")
print(f"{list(z) = }")
print('-' * 60)

# for index, element in enumerate(ITERABLE):
for i, color in enumerate(colors):
    print(i, color)
print()
print(f"{list(enumerate(colors)) = }")
print()

# range(stop-before)  range(start-at, stop-before) 
# range(start-at, stop-before, count-by)
r1 = range(1, 11)   #  1 to 10
r2 = range(10)      #  0 to 9

for value in r1:
    print(value)
print()

for i in range(2, 31, 2):
    print(i, end=" ")
print("\n")


