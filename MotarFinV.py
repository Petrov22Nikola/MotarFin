from random import randint
from statistics import mode, StatisticsError
scheme = input("Engine plays white(W) or black(B): ")
letters = ["A","B","C","D","E","F","G","H"]
numbers = ["1","2","3","4","5","6","7","8"]
board = []
history = []
turn = 0
legalmau = []
checked = False
incognito = False
#Inital Board Position:
#Board & Pawns
for i in range(8):
  for k in range(8):
    if k == 1:
      col = "W"
    elif k == 6:
      col = "B"
    else:
      col = ""
    if k == 1 or k == 6:
      board.append(letters[i] + numbers[k] + col)
    else:
      board.append(letters[i] + numbers[k])

#Rooks
board[0] += "WR"
board[7] += "BR"
board[56] += "WR"
board[63] += "BR"

#Knights
board[8] += "WN"
board[15] += "BN"
board[48] += "WN"
board[55] += "BN"

#Bishops
board[16] += "WB"
board[23] += "BB"
board[40] += "WB"
board[47] += "BB"

#Kings & Queens
board[24] += "WQ"
board[31] += "BQ"
board[32] += "WK"
board[39] += "BK"
#Inital Board Position Set

#Judicial System (Legal Moves)
legalma = []
KCastle = True
TKC = True
QCastle = True
TQC = True
BKCastle = True
TBKC = True
BQCastle = True
TBQC = True
def legalmoves():
  for i in range(64):
    Ncolour = None
    Bcolour = None
    Rcolour = None
    Qcolour = None
    Kcolour = None
    if len(board[i]) > 2:
      #White Pawns
      if turn % 2 == 0:
        if board[i][2:] == "W":
          if len(board[i + 1]) == 2:
            if float(board[i + 1][1]) != 8:
              legalma.append(board[i]+"-"+board[i + 1])
            else:
              legalma.append(board[i]+"-"+board[i + 1]+"-"+"WQ")
              legalma.append(board[i]+"-"+board[i + 1]+"-"+"WN")
              legalma.append(board[i]+"-"+board[i + 1]+"-"+"WB")
              legalma.append(board[i]+"-"+board[i + 1]+"-"+"WR")
          if len(board[i + 2]) == 2 and len(board[i + 1]) == 2 and board[i][1:-1] == "2":
            legalma.append(board[i]+"-"+board[i + 2])
          if board[i][0] != "A":
            if len(board[i - 7]) > 2 and board[i - 7][2] != "W":
              if float(board[i - 7][1]) != 8:
                legalma.append(board[i]+"-"+board[i - 7])
              else:
                legalma.append(board[i]+"-"+board[i - 7]+"-"+"WQ")
                legalma.append(board[i]+"-"+board[i - 7]+"-"+"WN")
                legalma.append(board[i]+"-"+board[i - 7]+"-"+"WB")
                legalma.append(board[i]+"-"+board[i - 7]+"-"+"WR")
          if board[i][0] != "H":
            if len(board[i + 9]) > 2 and board[i + 9][2] != "W":
              if float(board[i + 9][1]) != 8:
                legalma.append(board[i]+"-"+board[i + 9])
              else:
                legalma.append(board[i]+"-"+board[i + 9]+"-"+"WQ")
                legalma.append(board[i]+"-"+board[i + 9]+"-"+"WN")
                legalma.append(board[i]+"-"+board[i + 9]+"-"+"WB")
                legalma.append(board[i]+"-"+board[i + 9]+"-"+"WR")
          #En Passant
          if len(history) != 0:
            if history[-1] == "A7B-A5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-A6")
          if len(history) != 0:
            if history[-1] == "B7B-B5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-B6")
          if len(history) != 0:
            if history[-1] == "C7B-C5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-C6")
          if len(history) != 0:
            if history[-1] == "D7B-D5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-D6")
          if len(history) != 0:
            if history[-1] == "E7B-E5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-E6")
          if len(history) != 0:
            if history[-1] == "F7B-F5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-F6")
          if len(history) != 0:
            if history[-1] == "G7B-G5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-G6")
          if len(history) != 0:
            if history[-1] == "H7B-H5":
              if board[i][1] == "5":
                legalma.append(board[i]+"-H6")
      #Black Pawns
      if turn % 2 == 1:
        if board[i][2:] == "B":
          if len(board[i - 1]) == 2:
            if float(board[i - 1][1]) != 1:
              legalma.append(board[i]+"-"+board[i - 1])
            else:
              legalma.append(board[i]+"-"+board[i - 1]+"-"+"BQ")
              legalma.append(board[i]+"-"+board[i - 1]+"-"+"BN")
              legalma.append(board[i]+"-"+board[i - 1]+"-"+"BB")
              legalma.append(board[i]+"-"+board[i - 1]+"-"+"BR")
          if len(board[i - 2]) == 2 and len(board[i - 1]) == 2 and board[i][1:-1] == "7":
            legalma.append(board[i]+"-"+board[i - 2])
          if board[i][0] != "H":
            if len(board[i + 7]) > 2 and board[i + 7][2] != "B":
              if float(board[i + 7][1]) != 1:
                legalma.append(board[i]+"-"+board[i + 7])
              else:
                legalma.append(board[i]+"-"+board[i + 7]+"-"+"BQ")
                legalma.append(board[i]+"-"+board[i + 7]+"-"+"BN")
                legalma.append(board[i]+"-"+board[i + 7]+"-"+"BB")
                legalma.append(board[i]+"-"+board[i + 7]+"-"+"BR")
          if board[i][0] != "A":
            if len(board[i - 9]) > 2 and board[i - 9][2] != "B":
              if float(board[i - 9][1]) != 1:
                legalma.append(board[i]+"-"+board[i - 9])
              else:
                legalma.append(board[i]+"-"+board[i - 9]+"-"+"BQ")
                legalma.append(board[i]+"-"+board[i - 9]+"-"+"BN")
                legalma.append(board[i]+"-"+board[i - 9]+"-"+"BB")
                legalma.append(board[i]+"-"+board[i - 9]+"-"+"BR")
          #En Passant
          if len(history) != 0:
            if history[-1] == "A2W-A4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-A3")
          if len(history) != 0:
            if history[-1] == "B2W-B4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-B3")
          if len(history) != 0:
            if history[-1] == "C2W-C4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-C3")
          if len(history) != 0:
            if history[-1] == "D2W-D4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-D3")
          if len(history) != 0:
            if history[-1] == "E2W-E4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-E3")
          if len(history) != 0:
            if history[-1] == "F2W-F4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-F3")
          if len(history) != 0:
            if history[-1] == "G2W-G4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-G3")
          if len(history) != 0:
            if history[-1] == "H2W-H4":
              if board[i][1] == "4":
                legalma.append(board[i]+"-H3")
      #Knights
      if turn % 2 == 1:
        if board[i][2:] == "BN":
          Ncolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WN":
          Ncolour = "W"
      if Ncolour != None:
        if float(board[i][1]) != 8:
          if i + 17 < 64:
            if len(board[i + 17]) == 2:
              legalma.append(board[i]+"-"+board[i + 17])
            elif board[i + 17][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i + 17])
          if i - 15 >= 0:
            if len(board[i - 15]) == 2:
              legalma.append(board[i]+"-"+board[i - 15])
            elif board[i - 15][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i - 15])
        if float(board[i][1]) != 1:
          if i + 15 < 64:
            if len(board[i + 15]) == 2:
              legalma.append(board[i]+"-"+board[i + 15])
            elif board[i + 15][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i + 15])
          if i - 17 >= 0:
            if len(board[i - 17]) == 2:
              legalma.append(board[i]+"-"+board[i - 17])
            elif board[i - 17][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i - 17])
        if float(board[i][1]) < 7:
          if i - 6 >= 0:
            if len(board[i - 6]) == 2:
              legalma.append(board[i]+"-"+board[i - 6])
            elif board[i - 6][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i - 6])
          if i + 10 < 64:
            if len(board[i + 10]) == 2:
              legalma.append(board[i]+"-"+board[i + 10])
            elif board[i + 10][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i + 10])
        if float(board[i][1]) > 2:
          if i - 10 >= 0:
            if len(board[i - 10]) == 2:
              legalma.append(board[i]+"-"+board[i - 10])
            elif board[i - 10][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i - 10])
          if i + 6 < 64:
            if len(board[i + 6]) == 2:
              legalma.append(board[i]+"-"+board[i + 6])
            elif board[i + 6][2] != Ncolour:
              legalma.append(board[i]+"-"+board[i + 6])
      #Bishops
      if turn % 2 == 1:
        if board[i][2:] == "BB":
          Bcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WB":
          Bcolour = "W"
      if Bcolour != None and float(board[i][1]) != 8:
        for k in range(9):
          num = 7
          if i - k*num >= 0 and k != 0:
            if len(board[i - k*num]) > 2 and board[i - k*num][2] == Bcolour:
              break
            if len(board[i - k*num]) == 2:
              legalma.append(board[i]+"-"+board[i - k*num])
              if board[i - k*num][1] == "8":
                break
            if len(board[i - k*num]) > 2 and board[i - k*num][2] != Bcolour:
              legalma.append(board[i]+"-"+board[i - k*num])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BB":
          Bcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WB":
          Bcolour = "W"
      if Bcolour != None and float(board[i][1]) != 8:
        for k in range(9):
          num = 9
          if i + k*num < 64 and k != 0:
            if len(board[i + k*num]) > 2 and board[i + k*num][2] == Bcolour:
              break
            if len(board[i + k*num]) == 2:
              legalma.append(board[i]+"-"+board[i + k*num])
              if board[i + k*num][1] == "8":
                break
            if len(board[i + k*num]) > 2 and board[i + k*num][2] != Bcolour:
              legalma.append(board[i]+"-"+board[i + k*num])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BB":
          Bcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WB":
          Bcolour = "W"
      if Bcolour != None and float(board[i][1]) != 1:
        for k in range(9):
          num = 9
          if i - k*num >= 0 and k != 0:
            if len(board[i - k*num]) > 2 and board[i - k*num][2] == Bcolour:
              break
            if len(board[i - k*num]) == 2:
              legalma.append(board[i]+"-"+board[i - k*num])
              if board[i - k*num][1] == "1":
                break
            if len(board[i - k*num]) > 2 and board[i - k*num][2] != Bcolour:
              legalma.append(board[i]+"-"+board[i - k*num])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BB":
          Bcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WB":
          Bcolour = "W"
      if Bcolour != None and float(board[i][1]) != 1:
        for k in range(9):
          num = 7
          if i + k*num < 64 and k != 0:
            if len(board[i + k*num]) > 2 and board[i + k*num][2] == Bcolour:
              break
            if len(board[i + k*num]) == 2:
              legalma.append(board[i]+"-"+board[i + k*num])
              if board[i + k*num][1] == "1":
                break
            if len(board[i + k*num]) > 2 and board[i + k*num][2] != Bcolour:
              legalma.append(board[i]+"-"+board[i + k*num])
              break
      #Rooks
      if turn % 2 == 1:
        if board[i][2:] == "BR":
          Rcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WR":
          Rcolour = "W"
      if Rcolour != None and float(board[i][1]) != 8:
        for k in range(9 - int(board[i][1])):
          if i + k < 64 and k != 0:
            if len(board[i + k]) > 2 and board[i + k][2] == Rcolour:
              break
            if len(board[i + k]) == 2:
              legalma.append(board[i]+"-"+board[i + k])
              if board[i + k][1] == "8":
                break
            if len(board[i + k]) > 2 and board[i + k][2] != Rcolour:
              legalma.append(board[i]+"-"+board[i + k])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BR":
          Rcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WR":
          Rcolour = "W"
      if Rcolour != None and float(board[i][1]) != 1:
        for k in range(int(board[i][1])+1):
          if i - k >= 0 and k != 0:
            if len(board[i - k]) > 2 and board[i - k][2] == Rcolour:
              break
            if len(board[i - k]) == 2:
              legalma.append(board[i]+"-"+board[i - k])
              if board[i - k][1] == "1":
                break
            if len(board[i - k]) > 2 and board[i - k][2] != Rcolour:
              legalma.append(board[i]+"-"+board[i - k])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BR":
          Rcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WR":
          Rcolour = "W"
      if Rcolour != None and board[i][0] != "A":
        for k in range(9):
          if i - k*8 >= 0 and k != 0:
            if len(board[i - k*8]) > 2 and board[i - k*8][2] == Rcolour:
              break
            if len(board[i - k*8]) == 2:
              legalma.append(board[i]+"-"+board[i - k*8])
            if len(board[i - k*8]) > 2 and board[i - k*8][2] != Rcolour:
              legalma.append(board[i]+"-"+board[i - k*8])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BR":
          Rcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WR":
          Rcolour = "W"
      if Rcolour != None and board[i][0] != "H":
        for k in range(9):
          if i + k*8 < 64 and k != 0:
            if len(board[i + k*8]) > 2 and board[i + k*8][2] == Rcolour:
              break
            if len(board[i + k*8]) == 2:
              legalma.append(board[i]+"-"+board[i + k*8])
            if len(board[i + k*8]) > 2 and board[i + k*8][2] != Rcolour:
              legalma.append(board[i]+"-"+board[i + k*8])
              break
      #Queen
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and float(board[i][1]) != 8:
        for k in range(9 - int(board[i][1])):
          if i + k < 64 and k != 0:
            if len(board[i + k]) > 2 and board[i + k][2] == Qcolour:
              break
            if len(board[i + k]) == 2:
              legalma.append(board[i]+"-"+board[i + k])
            if len(board[i + k]) > 2 and board[i + k][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i + k])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and float(board[i][1]) != 1:
        for k in range(int(board[i][1])):
          if i - k >= 0 and k != 0:
            if len(board[i - k]) > 2 and board[i - k][2] == Qcolour:
              break
            if len(board[i - k]) == 2:
              legalma.append(board[i]+"-"+board[i - k])
            if len(board[i - k]) > 2 and board[i - k][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i - k])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and board[i][0] != "A":
        for k in range(9):
          if i - k*8 >= 0 and k != 0:
            if len(board[i - k*8]) > 2 and board[i - k*8][2] == Qcolour:
              break
            if len(board[i - k*8]) == 2:
              legalma.append(board[i]+"-"+board[i - k*8])
            if len(board[i - k*8]) > 2 and board[i - k*8][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i - k*8])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and board[i][0] != "H":
        for k in range(9):
          if i + k*8 < 64 and k != 0:
            if len(board[i + k*8]) > 2 and board[i + k*8][2] == Qcolour:
              break
            if len(board[i + k*8]) == 2:
              legalma.append(board[i]+"-"+board[i + k*8])
            if len(board[i + k*8]) > 2 and board[i + k*8][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i + k*8])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and float(board[i][1]) != 8:
        for k in range(9):
          num = 7
          if i - k*num >= 0 and k != 0:
            if len(board[i - k*num]) > 2 and board[i - k*num][2] == Qcolour:
              break
            if len(board[i - k*num]) == 2:
              legalma.append(board[i]+"-"+board[i - k*num])
              if board[i - k*num][1] == "8":
                break
            if len(board[i - k*num]) > 2 and board[i - k*num][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i - k*num])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and float(board[i][1]) != 8:
        for k in range(9):
          num = 9
          if i + k*num < 64 and k != 0:
            if len(board[i + k*num]) > 2 and board[i + k*num][2] == Qcolour:
              break
            if len(board[i + k*num]) == 2:
              legalma.append(board[i]+"-"+board[i + k*num])
              if board[i + k*num][1] == "8":
                break
            if len(board[i + k*num]) > 2 and board[i + k*num][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i + k*num])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and float(board[i][1]) != 1:
        for k in range(9):
          num = 9
          if i - k*num >= 0 and k != 0:
            if len(board[i - k*num]) > 2 and board[i - k*num][2] == Qcolour:
              break
            if len(board[i - k*num]) == 2:
              legalma.append(board[i]+"-"+board[i - k*num])
              if board[i - k*num][1] == "1":
                break
              if board[i - k*num][1] == "1":
                break
            if len(board[i - k*num]) > 2 and board[i - k*num][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i - k*num])
              break
      if turn % 2 == 1:
        if board[i][2:] == "BQ":
          Qcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WQ":
          Qcolour = "W"
      if Qcolour != None and float(board[i][1]) != 1:
        for k in range(9):
          num = 7
          if i + k*num < 64 and k != 0:
            if len(board[i + k*num]) > 2 and board[i + k*num][2] == Qcolour:
              break
            if len(board[i + k*num]) == 2:
              legalma.append(board[i]+"-"+board[i + k*num])
              if board[i + k*num][1] == "1":
                break
              if board[i + k*num][1] == "1":
                break
            if len(board[i + k*num]) > 2 and board[i + k*num][2] != Qcolour:
              legalma.append(board[i]+"-"+board[i + k*num])
              break
      #King
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and float(board[i][1]) != 8:
        if len(board[i + 1]) == 2:
          legalma.append(board[i]+"-"+board[i + 1])
        if len(board[i + 1]) > 2 and board[i + 1][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i + 1])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and float(board[i][1]) != 1:
        if len(board[i - 1]) == 2:
          legalma.append(board[i]+"-"+board[i - 1])
        if len(board[i - 1]) > 2 and board[i - 1][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i - 1])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and board[i][0] != "H":
        if len(board[i + 8]) == 2:
          legalma.append(board[i]+"-"+board[i + 8])
        if len(board[i + 8]) > 2 and board[i + 8][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i + 8])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and board[i][0] != "A":
        if len(board[i - 8]) == 2:
          legalma.append(board[i]+"-"+board[i - 8])
        if len(board[i - 8]) > 2 and board[i - 8][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i - 8])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and board[i][0] != "H":
        if len(board[i + 8]) == 2:
          legalma.append(board[i]+"-"+board[i + 8])
        if len(board[i + 8]) > 2 and board[i + 8][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i + 8])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and i - 7 >= 0 and float(board[i][1]) != 8:
        if len(board[i - 7]) == 2:
          legalma.append(board[i]+"-"+board[i - 7])
        if len(board[i - 7]) > 2 and board[i - 7][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i - 7])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and i - 9 >= 0 and float(board[i][1]) != 1:
        if len(board[i - 9]) == 2:
          legalma.append(board[i]+"-"+board[i - 9])
        if len(board[i - 9]) > 2 and board[i - 9][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i - 9])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and i + 7 < 64 and float(board[i][1]) != 1:
        if len(board[i + 7]) == 2:
          legalma.append(board[i]+"-"+board[i + 7])
        if len(board[i + 7]) > 2 and board[i + 7][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i + 7])
      if turn % 2 == 1:
        if board[i][2:] == "BK":
          Kcolour = "B"
      if turn % 2 == 0:
        if board[i][2:] == "WK":
          Kcolour = "W"
      if Kcolour != None and i + 9 < 64 and float(board[i][1]) != 8:
        if len(board[i + 9]) == 2:
          legalma.append(board[i]+"-"+board[i + 9])
        if len(board[i + 9]) > 2 and board[i + 9][2] != Kcolour:
          legalma.append(board[i]+"-"+board[i + 9])
      #Castling
      if Kcolour == "W":
        if KCastle == True and board[40] == "F1" and board[48] == "G1" and TKC == True and board[32] == "E1WK" and board[56] == "H1WR":
          legalma.append("W0-0")
        if QCastle == True and board[8] == "B1" and board[16] == "C1" and board[24] == "D1" and TQC == True and board[32] == "E1WK" and board[0] == "A1WR":
          legalma.append("W0-0-0")
      if Kcolour == "B":
        if BKCastle == True and board[47] == "F8" and board[55] == "G8" and TBKC == True and board[39] == "E8BK" and board[63] == "H8BR":
          legalma.append("B0-0")
        if BQCastle == True and board[15] == "B8" and board[23] == "C8" and board[31] == "D8" and TBQC == True and board[39] == "E8BK" and board[7] == "A8BR":
          legalma.append("B0-0-0")

legalmoves()

#Movement Function
def makemove(choice):
  if True:
    move = choice.split("-")
    if choice in legalmit:
      if incognito == False:
        history.append(choice)
      if choice[0] != "B" or choice[0] != "W":
        if len(move[0]) > 2:
          locd = board.index(move[0])
          loca = board.index(move[1])
          if len(board[loca]) > 2:
            board[loca] = board[loca][:-1*(len(board[loca])-2)]
          if len(move) == 2:
            board[loca] += board[locd][2:]
          else:
            board[loca] += move[2]
          board[locd] = board[locd][:-1*(len(board[locd])-2)]
          if incognito == False:
            if choice == "B5W-A6":
              board[4] = "A5"
            if choice == "A5W-B6" or choice == "C5W-B6":
              board[12] = "B5"
            if choice == "B5W-C6" or choice == "D5W-C6":
              board[20] = "C5"
            if choice == "C5W-D6" or choice == "E5W-D6":
              board[28] = "D5"
            if choice == "D5W-E6" or choice == "F5W-E6":
              board[36] = "E5"
            if choice == "E5W-F6" or choice == "G5W-F6":
              board[44] = "F5"
            if choice == "H5W-G6" or choice == "F5W-G6":
              board[52] = "G5"
            if choice == "G5W-H6":
              board[60] = "H5"
            if choice == "B4W-A3":
              board[3] = "A4"
            if choice == "A4W-B3" or choice == "C4W-B3":
              board[11] = "B4"
            if choice == "B4W-C3" or choice == "D4W-C3":
              board[19] = "C4"
            if choice == "C4W-D3" or choice == "E4W-D3":
              board[27] = "D4"
            if choice == "D4W-E3" or choice == "F4W-E3":
              board[35] = "E4"
            if choice == "E4W-F3" or choice == "G4W-F3":
              board[43] = "F4"
            if choice == "H4W-G3" or choice == "F4W-G3":
              board[51] = "G4"
            if choice == "G4W-H3":
              board[59] = "H4"
            if choice[2] == "W" and choice[3] == "K":
              QCastle = False
              KCastle = False
            if choice[2] == "B" and choice[3] == "K":
              BQCastle = False
              BKCastle = False
            if choice[2] == "W" and choice[3] == "R" and choice[0] == "H":
              KCastle = False
            if choice[2] == "B" and choice[3] == "R" and choice[0] == "H":
              BKCastle = False
            if choice[2] == "W" and choice[3] == "R" and choice[0] == "A":
              QCastle = False
            if choice[2] == "B" and choice[3] == "R" and choice[0] == "A":
              BQCastle = False
        else:
          if choice == "W0-0":
            board[48] += "WK"
            board[40] += "WR"
            board[56] = "H1"
            board[32] = "E1"
          if choice == "B0-0":
            board[55] += "BK"
            board[47] += "BR"
            board[63] = "H8"
            board[39] = "E8"
          if choice == "B0-0-0":
            board[23] += "BK"
            board[31] += "BR"
            board[7] = "A8"
            board[39] = "E8"
          if choice == "W0-0-0":
            board[16] += "WK"
            board[24] += "WR"
            board[0] = "A1"
            board[32] = "E1"

def legalmovesV2():
  #Check Prevention
  global turn
  global board
  global legalmit
  global checked
  global incognito
  legalma[:] = []
  legalmau[:] = []
  turn += 1
  legalmoves()
  turn -= 1
  checked = False
  for k in range(len(legalma)):
    if legalma[k].count("-") == 1:
      if legalma[k].endswith("K"):
        checked = True
    else:
      if legalma[k][:-3].endswith("K"):
        checked = True
  legalma[:] = []
  legalmoves()
  boardcopy = board[:]
  if checked == True:
    legalmit = legalma[:]
    for j in range(len(legalmit)):
      board = boardcopy[:]
      incognito = True
      makemove(legalmit[j])
      legalma[:] = []
      turn += 1
      legalmoves()
      turn -= 1
      for m in range(len(legalma)):
        if legalma[m].count("-") == 1:
          if legalma[m].endswith("K"):
            legalmau.append(legalmit[j])
        else:
          if legalma[m][:-3].endswith("K"):
            legalmau.append(legalmit[j])
  board = boardcopy[:]
  incognito = False
  #Pinned Pieces
  legalma[:] = []
  legalmoves()
  boardcopy = board[:]
  legalmit = legalma[:]
  for p in range(len(legalmit)):
    board = boardcopy[:]
    incognito = True
    makemove(legalmit[p])
    legalma[:] = []
    turn += 1
    legalmoves()
    turn -= 1
    for m in range(len(legalma)):
      if legalma[m].endswith("K"):
        legalmau.append(legalmit[p])
  board = boardcopy[:]
  incognito = False
  legalma[:] = []
  legalmoves()
  legalmit = legalma[:]
  for d in range(len(legalmau)):
    if legalmau[d] in legalmit:
      legalmit.pop(legalmit.index(legalmau[d]))
  board = boardcopy[:]

def comeval():
  global evaluation
  global turn
  evaluation = 0
  turn += 1
  legalmoves()
  legalmovesV2()
  turn -= 1
  for re in range(len(legalmit)):
    if turn % 2 == 0:
      if legalmit[re].endswith("N"):
        evaluation -= 3
    else:
      if legalmit[re].endswith("N"):
        evaluation += 3
    if turn % 2 == 0:
      if legalmit[re].endswith("Q"):
        evaluation -= 9
    else:
      if legalmit[re].endswith("Q"):
        evaluation += 9
    if turn % 2 == 0:
      if legalmit[re].endswith("R"):
        evaluation -= 5
    else:
      if legalmit[re].endswith("R"):
        evaluation += 5
    if turn % 2 == 0:
      if legalmit[re][len(legalmit[re])-2:] == "WB":
        evaluation -= 3
    else:
      if legalmit[re][len(legalmit[re])-2:] == "BB":
        evaluation += 3
    if turn % 2 == 0:
      if legalmit[re].endswith("W"):
        evaluation -= 3
    else:
      if legalmit[re].endswith("B"):
        if legalmit[re][:-1].endswith("W") or legalmit[re][:-1].endswith("B"):
          evaluation = evaluation
        else:
          evaluation += 3
  for e in range(64):
    if board[e] == "E3W" or board[e] == "E4W" or board[e] == "D3W" or board[e] == "D4W" or board[e] == "C3WN" or board[e] == "F3WN" or board[e] == "E2WB":
      evaluation += 0.5
    if board[e] == "E6B" or board[e] == "E5B" or board[e] == "D6B" or board[e] == "D5B" or board[e] == "C6BN" or board[e] == "F6BN" or board[e] == "E7BB":
      evaluation -= 0.5
    if board[e] == "G1WK":
      evaluation += 1
    if board[e] == "G8BK":
      evaluation -= 1
    if len(board[e]) == 3:
      if board[e].endswith("W"):
        evaluation += 1
      if board[e].endswith("B"):
        evaluation -= 1
    if len(board[e]) == 4:
      if board[e][2:] == "WR":
        evaluation += 5
      if board[e][2:] == "BR":
        evaluation -= 5
      if board[e][2:] == "WB":
        evaluation += 3
      if board[e][2:] == "BB":
        evaluation -= 3
      if board[e][2:] == "WN":
        evaluation += 3
      if board[e][2:] == "BN":
        evaluation -= 3
      if board[e][2:] == "WQ":
        evaluation += 9
      if board[e][2:] == "BQ":
        evaluation -= 9

#Evaluate Position
def evalposition():
  global board
  global incognito
  global meilleur
  global average
  global legalmit
  global baguette
  average = 0
  positions = []
  values = []
  meilleur = []
  mvalues = []
  valeur = 0
  baguette = ""
  boardcopy = board[:]
  legalmoves()
  legalmovesV2()
  legalwit = legalmit[:]
  for u in range(len(legalwit)):
    incognito = True
    board = boardcopy[:]
    makemove(legalwit[u])
    legalya = legalmit[:]
    comeval()
    legalmit = legalya[:]
    positions.append(legalwit[u])
    values.append(evaluation)
  for y in range(len(values)):
    average += values[y]
  if len(legalwit) != 0:
    average = average/len(legalwit)
  for r in range(len(values)):
    try:
      muffin = mode(values)
    except StatisticsError:
      muffin = values[0]
    if turn % 2 == 0:
      if values[r] > average and values[r] > muffin:
        meilleur.append(positions[r])
        mvalues.append(values[r])
    else:
      if values[r] < average and values[r] < muffin:
        meilleur.append(positions[r])
        mvalues.append(values[r])
  for w in range(len(meilleur)):
    if w == 0:
      baguette = meilleur[w]
      valeur = mvalues[w]
    if turn % 2 == 0:
      if mvalues[w] > valeur:
        baguette = meilleur[w]
        valeur = mvalues[w]
    else:
      if mvalues[w] < valeur:
        baguette = meilleur[w]
        valeur = mvalues[w]
  incognito = False
  board = boardcopy[:]

#Movement
quit = False
while quit == False:
  legalmoves()
  legalmovesV2()
  TKC = True
  TQC = True
  TBKC = True
  TBQC = True
  legalma[:] = []
  turn += 1
  legalmoves()
  turn -= 1
  for w in range(len(legalma)):
    if legalma[w][len(legalma[w])-2:] == "F1" or legalma[w][len(legalma[w])-2:] == "G1":
      TKC = False
    if legalma[w][len(legalma[w])-2:] == "D1" or legalma[w][len(legalma[w])-2:] == "C1":
      TQC = False
    if legalma[w][len(legalma[w])-2:] == "F8" or legalma[w][len(legalma[w])-2:] == "G8":
      TBKC = False
    if legalma[w][len(legalma[w])-2:] == "D8" or legalma[w][len(legalma[w])-2:] == "C8":
      TBQC = False
  print("\n")
  legalmoves()
  legalmovesV2()
  if scheme.lower() == "b":
    if turn % 2 == 0:
      choice = input("Enter Piece & Location: ")
    else:
      if len(legalmit) != 0:
        evalposition()
        print("Moves Considered: ")
        print(meilleur)
        if len(legalmit) != 1:
          if len(meilleur) != 0:
            if baguette == None:
              random = randint(0,len(meilleur)-1)
              choice = meilleur[random]
            else:
              choice = baguette
          else:
            random = randint(0,len(legalmit)-1)
            choice = legalmit[random]
        else:
          choice = legalmit[0]
      else:
        print("Stalemate or Checkmate, you decide Im tired... Zzz...")
        choice = "q"
  if scheme.lower() == "w":
    if turn % 2 == 1:
      choice = input("Enter Piece & Location: ")
    else:
      legalmoves()
      legalmovesV2()
      if len(legalmit) != 0:
        evalposition()
        print("Moves Considered: ")
        print(meilleur)
        if len(legalmit) != 1:
          if len(meilleur) != 0:
            if baguette == None:
              random = randint(0,len(meilleur)-1)
              choice = meilleur[random]
            else:
              choice = baguette
          else:
            random = randint(0,len(legalmit)-1)
            choice = legalmit[random]
        else:
          choice = legalmit[0]
      else:
        print("Stalemate or Checkmate, you decide Im tired... Zzz...")
        choice = "q"
  #Checkmate/Stalemate
  legalma[:] = []
  legalmit[:] = []
  legalmoves()
  legalmovesV2()
  if len(legalmit) == 0:
    turn += 1
    legalmoves()
    turn -= 1
    checkmate = False
    for n in range(len(legalma)):
      if legalma[n].endswith("K"):
        print("Fine, fine, tis a checkmate Baguette!")
        checkmate = True
        break
    if checkmate == False:
      print("Fine, fine, tis a stalemate Baguette!")
  if choice.lower() == "q":
    quit = True
  else:
    legalma[:] = []
    legalmit[:] = []
    legalmoves()
    legalmovesV2()
    if choice in legalmit:
      makemove(choice)
      turn += 1
    else:
      print("Shrek is love, Shrek is life...")
  print("\n")
  print("Move History: ")
  print(history)
  print("\n")
  evalposition()
  print("Evaluation: ")
  print(evaluation)
  print("\n")
  print("Recommended Move: ")
  print(history[-1])
  print("Legal Moves: ")
  print(legalmit)
