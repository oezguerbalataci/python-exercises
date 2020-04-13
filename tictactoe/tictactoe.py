theTable = [["_","_","_"],
            ["_","_","_"],
            ["_","_","_"]]

def printTable(turn,a):
    if(a):
        if(turn %2 == 0):
            print("X's TURN :\n")
        else:
            print("O's TURN :\n ")
   
    print("       1     2     3" )
    print("   ------------------" )
    for i in range(0,3):
        print(str(i+1) + " |" ,end="")
        for j in range(0,3):
            print("    "+theTable[i][j] +" ",end="")
        print("\n")

def gameLoop():
    a = 1
    turn = 0
    while a:
        printTable(turn,a)
        coordX = int(input("give the x coord (between 1-3): "))
        coordY = int(input("give the y coord (between 1-3): "))
        if(coordX not in range(1,4) or coordY not in range(1,4) or type(coordX) != int or type(coordY) != int ):
            print("\nthe coordinates must be in range of 1-3")
            gameLoop()

        if(writeOnTable(coordX,coordY,turn)== True):
            writeOnTable(coordX,coordY,turn)
            turn +=1     
        else:
            print("\nthis position is already picked\n")
            continue
        
        if(winCheck() == "xT"):
            print("\n\nX WON :\n")
            a= 0
            printTable(turn,a)
            
        elif(winCheck()=="oT"):
            print("\n\nO WON\n")
            a = 0    
            printTable(turn,a)
  

def writeOnTable(x,y,turn):
    if (turn%2 == 0):
        if(theTable[x-1][y-1]=="_"):
            theTable[x-1][y-1] = "X"
            return True
    elif(turn %2 == 1):
        if(theTable[x-1][y-1]=="_"):
            theTable[x-1][y-1] = "O"
            return True
    else:
        return False

def winCheck():
    for t in range(0,3):
        counterRow = 0
        counterCol = 0
        for k in range(0,3):
            if(theTable[t][k]== "X"):
                counterRow +=1
            if(theTable[k][t]== "X"):
                counterCol += 1
        if (counterCol == 3 or counterRow==3):
            return "xT"
   
    for t in range(0,3):
        counterRow = 0
        counterCol = 0
        for k in range(0,3):
            if(theTable[t][k]== "X"):
                counterRow +=1
            if(theTable[k][t]== "O"):
                counterCol += 1
        if (counterCol == 3 or counterRow==3):
            return "oT"
   
    if(theTable[0][0]=="X" and theTable[1][1]=="X" and theTable[2][2]=="X" or
       theTable[0][2]=="X" and theTable[1][1]=="X" and theTable[2][0]=="X"):
       return "xT" 

    if(theTable[0][0]=="O" and theTable[1][1]=="O" and theTable[2][2]=="O" or
       theTable[0][2]=="O" and theTable[1][1]=="O" and theTable[2][0]=="O"):
       return "oT"

gameLoop()