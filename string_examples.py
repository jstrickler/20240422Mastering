s1 = "spam\n"   #  \n \t \r \f \b
s2 = 'spam\n'

a = "spam"
b = "ham"

print(a + b)
print("am" in a)
print("pm" in a)

print(len(a))
print(len(b))

person = "Billy Strings"
print(type(person))
x = person.upper()
print(x)
print(person.count('s'))
print(person.count('S'))
print(person.lower().count('s'))

print(person.endswith('s'))
print(person.removesuffix('s'))

s = "        wombat     "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

x = "%spam>"
print(x.strip('%>'))
m = "$1123.43"
print(m.lstrip('$'))
f = float(m.lstrip('$'))
print(f)

print(person)
print('ll' in person)
print(person.index('ll'))

print(person.replace('Billy', 'Bobby'))

name = "Doe,John"

tokens = name.split(',')
print(tokens)

name = "John Doe"
tokens = name.split()
print(tokens)

s = "xyxyxyyyyyyyyyyyyyyMy filthy ex lives in Texasxxxxxxyyyxxxyyx"
print(s.strip('xy'))
print(s.replace('x', '').replace('y', ''))
print(s.replace('xy', ''))




