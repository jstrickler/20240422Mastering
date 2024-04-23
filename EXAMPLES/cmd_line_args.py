
import sys   # Import the sys module 

print(sys.argv) # Print all parameters, including script itself
print("Script name (sys.argv[0])", sys.argv[0])

name = sys.argv[1]  # Get the first actual parameter
print("name is", name)
