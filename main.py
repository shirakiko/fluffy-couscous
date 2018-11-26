#此程序能输入学生成绩并能将其进行合理管理
#包括输入成绩，以表格的样子整齐地显示学生成绩，将成绩按照平均分排序三个功能
#第一个程序用以打印学生各科成绩，并将成绩给一个变量，让另外的程序调用
#这是主程序
import inputScore as lib
import showTable as lib2
import sortAndShowTable as lib3
#以上是对其他三个子程序的调用
scores = []
#上面建立了一个空列表，下面并设置了一个主函数，用以引导用户进入操作
def main():
    print("欢迎")
    print("m1=打印学生的成绩\nm2=以表格形式显示成绩\nm3=将成绩排序\n")
    while True:
        i = input('请选择你需要的操作: ')
        if i =='m1':
            scores = lib.inputScore()
        elif i =='m2':
            lib2.showTable(scores)
        elif i =='m3':
            lib3.sortAndShowTable(scores)
        else:
            break
main()

ex=input("请再按一次回车键退出")
