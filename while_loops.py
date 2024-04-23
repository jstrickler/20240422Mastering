i = 0
while i < 3:
    print(f"i is {i}")
    i += 1
print()

while True:   # "infinite" loop
    #  break -- exit the loop
    user_input = input("Enter a number or q to quit: ")
    if user_input == '':
        print("Please enter a number (or q to quit)")
        continue # -- got to top of loop
    if user_input == 'q':
        break
    number_value = float(user_input)
    print(f"{number_value = }")
    