import numpy as np

print("Welcome to Tic-Tac-Toe")
repeat= "yes"
winner=0
i=0
ok=False
while repeat == "yes":
    print("The board is a matrix 3x3, you can choose a position 1 to 9, beginnig for the left and top to rigth ")
    print(" 1 2 3 \n", "4 5 6 \n","7 8 9 \n" )
    board = [0,0,0,0,0,0,0,0,0]
    repeat1="x"

#Falta añadir que no se pueda sobrescribir si ya se ha hecho
    while i<9: 
            if i%2 == 0:
                Player1 = int(input("PLAYER1 Select a position, 1 to 9: " ))-1
                if Player1<0 or Player1>8:
                    print("Not posible position")
                    i=-1
                    ok=False
                else:
                    board[Player1]= 1
                    lastboard =[[board[0],board[1],board[2]],
                                [board[3],board[4],board[5]],
                                [board[6],board[7],board[8]]]
                    print(lastboard[0],lastboard[1],lastboard[2],sep='\n')
                    ok=True
                        
            elif i%2 == 1:
                Player2 = int(input("PLAYER2 Select a position, 1 to 9: "))-1
                if Player2<0 or Player2>8:
                    print("Not posible position")
                    i=0
                    ok=False
                else:
                    board[Player2]= 8
                    lastboard =[[board[0],board[1],board[2]],
                                [board[3],board[4],board[5]],
                                [board[6],board[7],board[8]]]
                    print(lastboard[0],lastboard[1],lastboard[2],sep='\n')
                    ok=True

            if  ok==True and (sum(lastboard[0])==3 or sum(lastboard[1])==3 or sum(lastboard[2])==3 or sum(lastboard[0:3][0])==3 or sum(lastboard[0:3][1])==3 or sum(lastboard[0:3][2])==3 or (lastboard[0][0]+lastboard[1][1]+lastboard[2][2])==3 or (lastboard[0][2]+lastboard[1][1]+lastboard[2][0])==3):
              print("Player1 ¡¡¡WINS!!")
              print(lastboard[0],lastboard[1],lastboard[2],sep='\n')
              winner=1
              break
            elif ok==True and (sum(lastboard[0])==24 or sum(lastboard[1])==24 or sum(lastboard[2])==24 or sum(lastboard[0:3][0])==24 or sum(lastboard[0:3][1])==24 or sum(lastboard[0:3][2])==24 or (lastboard[0][0]+lastboard[1][1]+lastboard[2][2])==24 or (lastboard[0][2]+lastboard[1][1]+lastboard[2][0])==24):
              print("Player2 ¡¡¡WINS!!")
              print(lastboard[0],lastboard[1],lastboard[2],sep='\n')
              winner=1
              break
            i=i+1

  
    if winner==0:
      print("TIE. NOBODY WIN :(")
    while repeat1.lower() != "y" and repeat1.lower() != "n" :
      repeat1=(input ("Do you want repeat? Y/N: "))
      if repeat1.lower() != "y" and repeat1.lower() != "n" :
          print("That's not an answer")
      else:
          if repeat1.lower() == "y":
              print("OK!, lets play!")
              repeat="yes"
          elif repeat1.lower()=="n":
              print("OK!, Good bye")
              repeat="no"
        

