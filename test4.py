import csv
 
def main():
    infile = open("story.csv", "r")
    csvReader = csv.reader(infile)
    line = infile.readline()

    lines = []
    
    print([0])
    for row in csvReader:
        lines.append(row)
    print(lines[0])
    
    infile.close()
main()