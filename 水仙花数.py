def daffodil(num):
    hundreds=int(num // 100)
    tens=int((num-hundreds*100) // 10)
    ones=num % 10
    s=hundreds*hundreds*hundreds+tens*tens*tens+ones*ones*ones
    if s==num:
        return num
    else:
        return 0
"""水仙花数的定义"""       

def size(num):
    if num<100 or num>+1000:
        return 0
    else:
        return num
"""判断输出的数字是不是满足范围条件"""

def main():
    num=int(input("Please enter a number.The number must from 100 to 999."))
    for i in range(100,size(num)+1):
        a=daffodil(i)
        if a!=0:
            print(a)
"""输入一个三位数，找出所有(100,该数字]的水仙花数"""       

a=input("Enter to begin.")        
while a!=0:
    main()



       
           
            
            
    
