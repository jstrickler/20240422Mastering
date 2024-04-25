d1 = dict()  # empty dict
d2 = {'m': 19, 'f': 150, 'b': 25}
d3 = {}  # empty dict

d2['r'] = 82
d2['a'] = 65
d2['m'] = 37
print(f"{d2 = }")
print()
d2['r'] = d2['r'] + 1
print(f"{d2 = }")
d2['r'] += 1
print(f"{d2 = }")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

airports['PHX'] = 'Phoenix'
print(f"{airports = }\n")


print(f"{airports['RDU'] = }")
print(f"{airports['MCI'] = }")
# print(f"{airports['LAX'] = }")
key = 'LAX'
if key in airports:
    print(f"{airports[key] = }")

print(f"{airports.get(key) = }")
print(f"{airports.get(key, 'Los Angeles') = }")
print(f"{airports = }")
print(f"{airports.setdefault(key, 'Los Angeles') = }")
print(f"{airports = }")

del airports['OAK']
del airports['SJC']
print(f"{airports = }")

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

print(f"{airports.items() = }")
print()
print(f"{airports.keys() = }")
print(f"{airports.values() = }")




