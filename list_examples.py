list1 = list()
list2 = ['a', 'b', 'm']
list3 = []  # empty list

cities = ['Clinton', 'Durham', 'Surprize', 'Norfolk', 'Columbia']
print(f"{cities = }")
cities.insert(0, "Raleigh")
cities.insert(3, "Phoenix")
print(f"{cities = }")
cities.append("Bowie")
cities.append("Takoma Park")
print(f"{cities = }")

x  = 'Durham'
print(x in cities)
print("Dubuque" in cities)
print(f"{cities.index(x) = }")

more_cities = ['Topeka', 'Topanga Canyon', 'Tacoma']
cities.extend(more_cities)
print(f"{cities = }")
# cities.append(more_cities)
# print(f"{cities = }")

#   LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)
del cities[9]   # del obj  del LIST[index]  del DICT[key]
print(f"{cities = }")

cities.remove('Topanga Canyon')
print(f"{cities = }")

city = cities.pop()
print(f"{city = }")
print(f"{cities = }")

city = cities.pop(3)
print(f"{city = }")
print(f"{cities = }")

#  del LIST[index]   LIST.remove(value)    LIST.pop()  LIST.pop(index)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[18] = }")
print(f"{fruits[21] = }")
print(f"{fruits[-1] = }")
print(f"{fruits[-3] = }")

person = "Humphrey Bogart"
print(f"{person[5] = }")
print(f"{person[-2] = }")

print(f"{fruits = }")


print(f"{fruits[0:4] = }")    # start-at 0  stop-before 4  count-by 1
print(f"{fruits[:4] = }")
print(f"{fruits[3:6] = }")
print(f"{fruits[::] = }")
print(f"{fruits[::2] = }")
print(f"{fruits[::3] = }")

print(f"{person[9:12] = }")

a=6
b=12
print(f"{fruits[a:b] = }")
print(f"{fruits[1:-1] = }")
print()

print(f"{fruits = }")
print()

for fruit in fruits:
    print(fruit.title())
print()

for fruit in fruits:
    print(fruit[:3].upper())

# for VAR in ITERABLE:
#    code ...





