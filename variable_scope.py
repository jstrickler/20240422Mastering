ANIMAL = 'wombat'  # global 

if ANIMAL:
    m = 'mugwump'

def spam(color):
    x = 10  # local 
    print(color * x)
    print(ANIMAL)

spam('red')

