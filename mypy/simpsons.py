import sys

def people_and_places("name"):


    if name == 'Lisa':
        print(name + " plays saxophone")
    elif name == 'Bart':
        print(name + " rides skateboard")
    elif name == 'Ruth':
        print(name + " resides in Salisbury aka Novichokland. jolly good jolly good jolly good.")
    elif name == 'Rachel':
        print(name + " is fae Waas which is ida bak o nowhere du kens. noo den noo den.")
    elif name == 'Dennis':
        print(name + " lives in Philly. alright alright alright.")
    else: 
        print(name + " lives in Springfield")

    return print("doh")


if __name__ == '__main__':
    arg = sys.argv[1:]
    
    for arg in args:
        people_and_places(arg)
