import sys

if len(sys.argv) < 3:
    print("please specify length and file path")
    sys.exit()

length = int(sys.argv[1])   # remove 1st arg (after script name)

file_path = sys.argv[2]

# syntax:  python find_long_words.py 20 DATA/words.txt

output_path = "longwords.txt"

with open(file_path) as file_in:  # read from words.txt
    with open(output_path, "w") as file_out:   # write to longwords.txt
        for raw_word in file_in:
            word = raw_word.rstrip()
            if len(word) >= length:
                file_out.write(raw_word)
                print(word)