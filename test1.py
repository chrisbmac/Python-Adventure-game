import csv

def options():
    print("hi")

def initial():
    print("1 - New Game")
    print

def userInput():
    player = int(input())


def get_file():
    
    with open('story.csv') as file:
        rows = list(csv.reader(file))
    for items in rows:
        if (items.isdigit()):
            print(items)
        return any(i.isdigit() for i in s)
        print(i)
    number = filter(str.isdigit, yourString)

    return file, rows

def initial():
    print("****** Text Adventure Game v1.0 ******")
    print("1 - New Game")
    print("2 - Load Game")
    print("3 - Quit ")
    print("***************************************")

get_file()
initial()
def options():
    fileinput = str(input("Which file do you want?"))
    if not ".csv" in fileinput:
        fileinput += ".csv"

def userInput():
    players_choices = set()
    rows, list = get_file()
    while True:
       try:
           Player = int(input("> "))
            
        except ValueError:
            print("Invalid Entry : Choose a number between 1-3")
       
    


    
    #return Player
     

