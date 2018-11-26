"""在函数中设计表格，靠设置间隔和位置来实现"""
#该程序以表格形式显示你的成绩
def showTable(sco):
    print('{0:<9}'.format('姓名'),end='')
    print('{0:^9}'.format('语文'),end='')
    print('{0:^9}'.format('数学'),end='')
    print('{0:^9}'.format('英语'),end='')
    print('{0:^9}'.format('物理'),end='')
    print('{0:^9}'.format('化学'),)
    for s in sco:
        print('{:<9}'.format(s['姓名']),end ='')
        print('{:^10}'.format(s['语文']),end ='')
        print('{:^10}'.format(s['数学']),end ='')
        print('{:^11}'.format(s['英语']),end ='')
        print('{:^10}'.format(s['物理']),end ='')
        print('{:^10}'.format(s['化学']),)
"""<表示顶格，^表示居中"""
