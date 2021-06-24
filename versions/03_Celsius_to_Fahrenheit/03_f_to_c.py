def to_c(from_f):
    celcius = (from_f - 32) * 5 / 9
    return celcius


# Main Routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    # {:.2f} to round number to 2 decimal places
    ans_statement = "{} degrees F is {:.2f} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)
