# Initial testing of saving list to .txt file
conversions_list = ["1", "2", "3"]
filename = input("Enter filename: ")
text_file = open(filename + ".txt", "w")
for element in conversions_list:
    text_file.write(element + "\n")
text_file.close()
