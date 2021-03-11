import csv
import operator
def get_file():
    
    with open('story.csv', 'r') as file:
        rows = list(csv.reader(file))
    return rows, file
def initial():
    print("****** Text Adventure Game v1.0 ******")
    print("1 - New Game")
    print("2 - Load Game")
    print("3 - Quit ")
    print("***************************************")

def main():
    rows, file = get_file()
    currrow = " "
    rowlist = []
    print(rows[0])
    user = int(input("enter: "))
    if user == 1:
        currrow =  in rows
        rowlist.append(rows)


initial()    
main()
