#!/usr/bin/python3
import csv
import copy

PL = "Premier League"
APL = "Premier League"
FA = "Football Association Challenge Cup"
EFL = "English Football League Cup"
UCL = "UEFA Champion League"
UEL = "UEFA Europa League"
CWC = "UEFA Cup Winners' Cup"
FCWC = "FIFA Club World Cup"

def season2year(season):
    return int(season.split('-')[0])

# 奖杯的数量
def cnt(filename):
    mp={}
    res={}
    x=filename.split(".")[0]
    print("const "+x+"_cnt=",end="")
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            team=row[1]
            if team in mp:
                mp[team]+=1
            else:
                mp[team]=1
            res[season]=copy.deepcopy(mp)
    print(res,end="")
    print(";")

# 年份列表
def title_list(filename):
    mp={}
    res={}
    x=filename.split(".")[0]
    print("const "+x+"_list=",end="")
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            team=row[1]
            if team in mp:
                mp[team].append(season)
            else:
                mp[team]=[]
                mp[team].append(season)
            res[season]=copy.deepcopy(mp)
    print(res,end="")
    print(";")

# 决赛比分
def final(filename):
    res={}
    x=filename.split(".")[0]
    print("const "+x+"_final=",end="")
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            data=row[1:4]
            if(season2year(season)>=1992):
                res[season]=data
    print(res,end="")
    print(";")

# 年份:球队
def title(filename):
    res={}
    x=filename.split(".")[0]
    print("const "+x+"_title=",end="")
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            if(season2year(season)>=1992):
                res[season]=row[1]
    print(res,end="")
    print(";")

# 某项赛事的最后一座冠军
def latest(filename):
    mp={}
    res={}
    x=filename.split(".")[0]
    print("const "+x+"_latest=",end="")
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            team=row[1]
            mp[team]=season
            if(season2year(season)>=1992):
                res[season]=copy.deepcopy(mp)
    print(res,end="")
    print(";")

# 所有赛事的最后一座冠军
def latest_all(* filenames):
    res={}
    print("const all_latest_all=",end="")
    for filename in filenames:
        title=filename.split(".")[0]
        with open(filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                season=row[0]
                team=row[1]
                if team in res:
                    if season2year(season)>season2year(res[team]["season"]):
                        x={}
                        x["season"]=season
                        x["title"]=eval(title)
                        res[team]=x
                else:
                    x={}
                    x["season"]=season
                    x["title"]=eval(title)
                    res[team]=x
    print(res,end="")
    print(";")

if __name__ == '__main__':
    cnt('PL.txt')

    title_list('UCL.txt')
    title_list('UEL.txt')
    title_list('CWC.txt')

    final('FA.txt')
    final('EFL.txt')

    title('PL.txt')
    title('UCL.txt')
    title('UEL.txt')
    title('FA.txt')
    title('EFL.txt')
    title('FCWC.txt')
    title('CWC.txt')

    latest('APL.txt')
    latest_all( "UCL.txt" ,"UEL.txt" ,"APL.txt","CWC.txt", "FCWC.txt","FA.txt", "EFL.txt"  )
