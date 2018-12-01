board = [['1','2','3'],['4','5','6'],['7','8','9']]

y= int(input("Please enter the 'y'"))
x= int(input("Please enter the 'x'"))
board[2][2]="x"

def hit(y,x):
    if board[y][x] == "x":
        print("Hit!")
        board[y][x] = "0"
    else:
        print("Please try again!")
        y= int(input("Please enter the 'y'"))
        x= int(input("Please enter the 'x'"))
        while board[y][x]!="0":
            hit(y,x)

     
hit(y,x)
