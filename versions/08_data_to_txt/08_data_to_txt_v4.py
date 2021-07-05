# Initial testing of saving list to .txt file

import re

conversions_list = ["1", "2", "3"]
has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter filename: ")
    has_error = "no"

    valid_file = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_file, filename):
            continue

        elif letter == " ":
            problem = "(spaces not allowed)"
        else:
            problem = ("({}s is not allowed)".format(letter))
        has_error = "yes"
        break

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
        print()
    else:
        print("You entered a valid filename")

text_file = open(filename + ".txt", "w")

for element in conversions_list:
    text_file.write(element + "\n")

text_file.close()
