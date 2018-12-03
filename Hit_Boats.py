board = [['1','2','3'],['4','5','6'],['7','8','9']]
#创建一个3x3的坐标格

a= int(input("Please set a coordinate for your boat."))
b= int(input("Please set the other one for it."))
board[a-1][b-1]="x"
#设定一个战舰的位置

("Now you can launch a missile to hit your enermy.")
y= int(input("Please enter the 'y'"))
x= int(input("Please enter the 'x'"))

while board[y-1][x-1]!="x":
    print("Please try again!")
    y= int(input("Please enter the 'y'"))
    x= int(input("Please enter the 'x'"))
else:
    print("Hit!")   
                      
       
#报出坐标击沉之

