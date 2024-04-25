
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

m = [1,2,3], [4, 5, 6]

x = 5,  # tuple containing one integer
y = 5   # integer

print(f"{person[0] = }")
print(f"{person[1] = }")
print(f"{person[:2] = }")

first_name, last_name, product, dob = person
print(f"{first_name = }")
print(f"{last_name = }")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', 'rsync', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]
print(f"{people[0] = }")
print(f"{people[0][1] = }")
print(f"{people[0][1][3] = }")
print()

#  for VAR1, VAR2 in ITERABLE:
#     ...
for first_name, last_name, *product, dob in people:
    print(last_name, product)
print()




