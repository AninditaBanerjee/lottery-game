

def acceptUserEntries():
    for i in range(0,6):
        print(i)
        currentEntry = int(input("enter a number "))
        userEntries[i] = currentEntry
        print(i+1,"number/s registered")
    #print (userEntries)


def generateRandomInt():
    print (len(random_Int))
    for i in range (0,len(random_Int)):
        random_Int[i]= random.randint(0,500)

def gamePlay():
    acceptUserEntries()
    generateRandomInt()
    print(random_Int)
    print(userEntries)
    for i in userEntries:
        for j in random_Int:
            #print(i)
            #print(j)
            if i == j:
                print("Yaay !!! You won :) ")
                quit()
    print ("Sorry you lost" )
    startGame()
   
def startGame():
    res = input("Do you want to gamble (y/n) ? ")
    if res == "y":
        res = gamePlay()

    else:
        quit()

    


import random
random_Int = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
userEntries=[0,0,0,0,0,0]

startGame()