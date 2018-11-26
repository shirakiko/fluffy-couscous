import tkinter as tk

win = tk.Tk()
win.title('Calculator')
"""设置窗口"""
def fun1(p):   
    ent.insert(tk.INSERT,p)
"""完成所有用按钮输入"""    
def cal():
    try:
        a=led.get()
        b=eval(a)
        led.set(b)
    except:
        led.set('E')
"""点击等于号完成运算，如果无法运算（如除以0），则输出E""" 
def cls():                      
    led.set("")
"""清除键(普通计算器中的C)"""
def dele():
    ent.delete(tk.INSERT)
"""撤销键（撤销后光标数字）"""
led=tk.StringVar()
ent= tk.Entry(win,textvariable=led)
ent.grid(row =0, columnspan=3)

but1 = tk.Button(win,text='1',width=5,command=lambda : fun1("1"))
but1.grid(row =1,column = 0)

but2 = tk.Button(win,text ='2',width=5,command=lambda:fun1("2"))
but2.grid(row =1,column = 1)

but3 = tk.Button(win,text ='3',width=5,command=lambda:fun1("3"))
but3.grid(row =1,column = 2)

but4 = tk.Button(win,text ='4',width=5,command=lambda:fun1("4"))
but4.grid(row =2,column = 0)

but5 = tk.Button(win,text ='5',width=5,command=lambda:fun1("5"))
but5.grid(row =2,column = 1)

but6 = tk.Button(win,text ='6',width=5,command=lambda:fun1("6"))
but6.grid(row =2,column = 2)

but7 = tk.Button(win,text ='7',width=5,command=lambda:fun1("7"))
but7.grid(row =3,column = 0)

but8 = tk.Button(win,text ='8',width=5,command=lambda:fun1("8"))
but8.grid(row =3,column = 1)

but9 = tk.Button(win,text ='9',width=5,command=lambda:fun1("9"))
but9.grid(row =3,column = 2)

but0 = tk.Button(win,text ='0',width=5,command=lambda:fun1("0"))
but0.grid(row =4,column = 1)

but_eql = tk.Button(win,text ='=',width=5,command=cal)
but_eql.grid(row =4,column = 2)

butCls = tk.Button(win,text ='cls',width=5,command=cls)
butCls.grid(row=4,column=0)

but_add =tk.Button(win,text='+',command=lambda: fun1('+'))
but_add.grid(row=5,column=0)

but_min =tk.Button(win,text='-',command=lambda :fun1('-'))
but_min.grid(row=5,column=1)

but_mul =tk.Button(win,text='x',command=lambda:fun1('*'))
but_mul.grid(row=5,column=2)

but_div =tk.Button(win,text='/',command=lambda: fun1('/'))
but_div.grid(row=6,column=0)

but_dot =tk.Button(win,text='.',command=lambda: fun1('.'))
but_dot.grid(row=6,column=2)

but_del =tk.Button(win,text="delete",command=dele)
but_del.grid(row=6,column=1)
"""设置各个按钮"""

win.mainloop()
"""程序循环运行"""

#报告发送到315350457@qq.com
