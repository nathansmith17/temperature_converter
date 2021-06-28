# Set up empty list
all_calc = []

# Get 5 items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calc.append(get_item)

all_calc.reverse()

# Show that everything appended correctly
print()
print("*** The Full List ***")
print(all_calc)

print()

print("*** Most Recent 3 ****")
for item in range(0, 3):
    print(all_calc[item])
