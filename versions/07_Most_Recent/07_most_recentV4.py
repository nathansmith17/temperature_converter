# Set up empty list
all_calc = []

# Get items of data and add to list
get_item = ""
while get_item != "q":
    get_item = input("Enter Item: ")

    if get_item == "q":
        break

    all_calc.append(get_item)

print()

if len(all_calc) == 0:
    print("List is empty")

else:

    # Show that everything appended correctly
    print()
    print("*** The Full List ***")
    print(all_calc)

    # print items starting at END of the list
    if len(all_calc) >= 3:
        print("*** Most Recent 3 ****")
        for item in range(0, 3):
            print(all_calc[len(all_calc) - item - 1])

    else:
        print("*** Items from Newest to Oldest ***")
        for item in all_calc:
            print(all_calc[len(all_calc) - all_calc.index(item) - 1])
