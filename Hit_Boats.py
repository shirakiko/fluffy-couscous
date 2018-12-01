board = [['1','2','3'],['4','5','6'],['7','8','9']]
#创建一个3x3的坐标格
y= int(input("Please enter the 'y'"))
x= int(input("Please enter the 'x'"))
board[2][2]="x"
#设定一个战舰的位置

while board[y][x]!="x":
    print("Please try again!")
    y= int(input("Please enter the 'y'"))
    x= int(input("Please enter the 'x'"))
else:
    print("Hit!")   
                      
       
#报出坐标击沉之

