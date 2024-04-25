
try:
    x = 5
    y = "cheese"
    z = x + y
    print(x / 0)
    f = open("sesame.txt")
    print("Bottom of try")

except (IOError, TypeError) as err:  # Use a tuple of 2 or more exception types
    print("Naughty programmer! ", err)
except IndexError as err:
    print(err)

print("ALL DONE")
