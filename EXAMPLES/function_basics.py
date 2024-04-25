

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()
print(get_hello())

def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print("m is {:.3f} n is {:.3f}".format(m, n))

def make_line(char, size=30):
    return char * size

line1 = make_line('*', 10)
print(line1)
line2 = make_line('=', 50)
print(line2)

def do_files(*file_paths):
    for file_path in file_paths:
        print(f"Processing {file_path}")

do_files()
print('-' * 60)
do_files('a.txt')
print('-' * 60)
do_files('a.txt', 'b.txt', 'c.txt')
print('-' * 60)

print(make_line('.'))


def spam(a, b, *c):
    print(f"{a = }")
    print(f"{b = }")
    print(f"{c = }")
    print('-' * 10)

spam(1, 2)
spam('up', 'down')
spam(5, 6, 7, 8, 19, 'wolverine', "Hobbit")

def print_matches(search_term, *file_paths, ignore_case=True):
    matches = []
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                search_line = raw_line.lower() if ignore_case else raw_line
                if search_term in search_line:
                    matches.append(raw_line.rstrip())
    return matches

found = print_matches('lizard', '../DATA/alice.txt', '../DATA/parrot.txt', ignore_case=False)
print(f"{found = }")
print()




