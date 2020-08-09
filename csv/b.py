#!/usr/bin/python3
import csv
import copy
import json

OUTPUT="../js/autogenerate.js"

PL = "Premier League"
APL = "Premier League"
FA = "Football Association Challenge Cup"
EFL = "English Football League Cup"
UCL = "UEFA Champion League"
UEL = "UEFA Europa League"
CWC = "UEFA Cup Winners' Cup"
FCWC = "FIFA Club World Cup"

# 2019-20 => 2019
def season2year(season):
    return int(season.split('-')[0])

# 奖杯的数量
def cnt(filename):
    mp={}
    res={}
    x=filename.split(".")[0]
    buffer="const "+x+"_cnt="
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
    buffer+=json.dumps(res)
    buffer+=";\n"
    return buffer

# 年份列表
def title_list(filename):
    mp={}
    res={}
    x=filename.split(".")[0]
    buffer= "const "+x+"_list="
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
    buffer+=json.dumps(res)
    buffer+=";\n"
    return buffer

# 决赛比分
def final(filename):
    res={}
    x=filename.split(".")[0]
    buffer="const "+x+"_final="
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            data=row[1:4]
            if(season2year(season)>=1992):
                res[season]=data
    buffer+=json.dumps(res)
    buffer+=";\n"
    return buffer

# 年份:球队
def title(filename):
    res={}
    x=filename.split(".")[0]
    buffer="const "+x+"_title="
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            if(season2year(season)>=1992):
                res[season]=row[1]
    buffer+=json.dumps(res)
    buffer+=";\n"
    return buffer

# 某项赛事的最后一座冠军
def latest(filename):
    mp={}
    res={}
    x=filename.split(".")[0]
    buffer="const "+x+"_latest="
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            team=row[1]
            mp[team]=season
            if(season2year(season)>=1992):
                res[season]=copy.deepcopy(mp)
    buffer+=json.dumps(res)
    buffer+=";\n"
    return buffer

# 所有赛事的最后一座冠军
def latest_all(* filenames):
    res={}
    buffer="const all_latest_all="
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
    buffer+=json.dumps(res)
    buffer+=";\n"
    return buffer

if __name__ == '__main__':
    s=""

    s+=cnt('PL.txt')

    s+=title_list('UCL.txt')
    s+=title_list('UEL.txt')
    s+=title_list('CWC.txt')

    s+=final('FA.txt')
    s+=final('EFL.txt')

    s+=title('PL.txt')
    s+=title('UCL.txt')
    s+=title('UEL.txt')
    s+=title('FA.txt')
    s+=title('EFL.txt')
    s+=title('FCWC.txt')
    s+=title('CWC.txt')

    s+=latest('APL.txt')
    s+=latest_all( "UCL.txt" ,"UEL.txt" ,"APL.txt","CWC.txt", "FCWC.txt","FA.txt", "EFL.txt"  )

    with open(OUTPUT,mode="w", encoding='utf-8') as f:
        f.write(s)
