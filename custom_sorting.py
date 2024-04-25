from dateutil.parser import parse

fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

def ignore_case(fruit):
    return fruit.lower()

f1 = sorted(fruits, key=ignore_case)
print(f"{f1 = }\n")

f2 = sorted(fruits, key=str.lower)
print(f"{f2 = }\n")

f3 = sorted(fruits, key=len)
print(f"{f3 = }\n")

def len_and_name(f):
    return len(f), f.lower()

f4 = sorted(fruits, key=len_and_name)
print(f"{f4 = }\n")

def wacky(x):
    return x[-1]

f5 = sorted(fruits, key=wacky, reverse=True)
print(f"{f5 = }\n")

#  lambda p, ...: value

f6 = sorted(fruits, key=lambda f: (f[-1]))
print(f"{f6 = }\n")

f7 = sorted(fruits, key=lambda e: (len(e), e.lower()))
print(f"{f7 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

people2 = [(p[0], p[1], p[2], parse(p[3]).date()) for p in people]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_company(p):
    sort_value = p[2], p[1], p[0]
    print(f"sorting {p} by {sort_value}")
    return sort_value

for person in sorted(people, key=by_company):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: p[3]):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: p[3], reverse=True):
    print(person)
print('-' * 60)

print(people2[0], '\n')

for person in sorted(people2, key=lambda p: p[3]):
    print(person)
print('-' * 60)

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

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

def by_value(element):
    return element[1], element[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print('-' * 60)
print(f"{fruits = }\n")
fruits.sort(key=str.lower)
print(f"{fruits = }")
