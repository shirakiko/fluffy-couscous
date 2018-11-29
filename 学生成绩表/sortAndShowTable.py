#用sort方法，以平均成绩将成绩排序
#现在开始将你的成绩排序并输出
def sortAndShowTable(sco):
    for i in sco:
        i['平均数']=(int(i['语文'])+int(i['数学'])+int(i['英语'])+int(i['物理'])+int(i['化学']))/5
    sco.sort(key=mykey,reverse=True)
    print(sco)
def mykey(a):
    return a['平均数']
    
