colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

c0 = []
for c in colors:
    value = c.upper()
    c0.append(value)
print(f"{c0 = }\n")

#     value     for-loop
c1 = [c.upper() for c in colors]  # list comprehension
print(f"{c1 = }\n")

c2 = [c.title() for c in colors if c.startswith('b')]
print(f"{c2 = }\n")

c3 = [c for c in colors if c.startswith('b')]
print(f"{c3 = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

n1 = [float(n) for n in nums if n > 300]
print(f"{n1 = }\n")

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

dobs = [(person[1], person[-1]) for person in people if person[0].startswith('L')]
print(f"{dobs = }\n")

dobs_gen = ((person[1], person[-1]) for person in people if person[0].startswith('L'))
print(f"{dobs_gen = }\n")

for dob in dobs_gen:
    print(dob, end=", ")
print("\n")


