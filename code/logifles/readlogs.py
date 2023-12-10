

def readfile(filename):
    file = open(filename, "r")

    rows = []

    # take each line in as a list object
    for line in file:
        # Remove whitespace
        line = line.replace(" ", "")
        rows.append(line.split((",")))

    # Convert parameters into a list
    for row in rows:
        # remove end of line character
        row[4] = row[4][:-3]

        # put params into a list
        row[4] = row[4].split(";")

    return rows

print(readfile("all-experiments.csv")[1])