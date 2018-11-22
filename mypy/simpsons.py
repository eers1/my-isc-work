import sys

def people_and_places(tup):
    name = tup[0]
    home = tup[1]


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
        print(name + " lives in " + home)

    return print(home * 3 + "!")


if __name__ == '__main__':
    args = sys.argv[1:]
#    args_srt = [(args[0],args[1]), (args[2],args[3])]
    args_srt = [args_srt.append((args[i], args[i + 1])) for i in args]

    print(args_srt)
    for arg in args_srt:        
        people_and_places(arg)
