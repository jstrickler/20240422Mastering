import sys

if len(sys.argv) < 2:
    print("please specify one or more temperatures on the command line")
    sys.exit()

for arg in sys.argv[1:]:
    try:
        celsius = float(arg)
    except ValueError as err:
        print("INVALID temperature!", err)
    else:
        fahrenheit = ((9 * celsius) / 5) + 32
    
    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

