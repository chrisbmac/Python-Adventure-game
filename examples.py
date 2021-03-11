import csv

name_to_search = input("type last name:")

with open("story.csv") as f:
    reader = csv.reader(f)

    # skip the first row, since it is header.
    #header = next(reader)
    found = False
    for line in reader:
        if name_to_search == line in f:
            print(line)
            found = True
            break
    if not found:
        print(name_to_search, "not found")