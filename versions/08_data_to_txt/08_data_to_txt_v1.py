# Initial testing of saving list to .txt file
conversions_list = ["1", "2", "3"]
filename_input = input("Enter filename: ")
filename = filename_input + ".txt"
text_file = open(filename, "w")
for element in conversions_list:
    text_file.write(element + "\n")
text_file.close()
