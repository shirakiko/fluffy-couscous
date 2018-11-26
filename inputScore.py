#创建一个空列表，并在里面加入字典
#该程序打印学生成绩
score = []

def inputScore():
    print('\n现在开始打印学生成绩')
    num = 0
    while True:
        s = {}
        sname = input('请输入学生的姓名: ')
        s['姓名']=sname
        yscore = input('请输入语文成绩: ')
        s['语文'] = yscore
        sxscore = input('请输入数学成绩: ')
        s['数学']= sxscore
        yyscore = input('请输入英语成绩: ')
        s['英语'] = yyscore
        wlscore = input('请输入物理成绩: ')
        s['物理'] = wlscore
        hxscore = input('请输入化学成绩: ')
        s['化学'] = hxscore
        
        score.append(s)
        print(score)
        num= num +1
        if num>4:
            return score
            break;
   
