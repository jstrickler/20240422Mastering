person = "Billy Strings"
city = "Nashville"
cost = 837.9393

print(person)
print(city)
print(cost)
print()
print(person, city, cost)
print()
print(person, city, cost, sep=',')
print()
print(person, city, cost, sep=', ')
print()
print(person, city, cost, sep='')
print()
print(person, end=" ")
print(city)
print()
print(person, ':', city)
print(person + ':', city)

print(f"{person}: {city}")   # current
print("{}: {}".format(person, city))  # legacy (3.0)
print("%s: %s" % (person, city))   # old (<2.6)
print("{person}: {city}")  # just wrong
print()
print(f"2 + 2 is {2 + 2}")
print(f"cost is {cost}")
print(f"cost is {cost:.2f}")
print("cost is {:.2f}".format(cost))


