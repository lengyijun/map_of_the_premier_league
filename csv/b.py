#!/usr/bin/python3
import csv
import copy
import json
from collections import defaultdict

OUTPUT="../js/autogenerate.js"
DERBY_OUTPUT="../js/derby.js"
FOUNDATION_OUTPUT="../js/foundation.js"

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
    mp=defaultdict(list)
    res={}
    x=filename.split(".")[0]
    buffer= "const "+x+"_list="
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            season=row[0]
            if season[0]=='#':
                continue
            team=row[1]
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
            if season[0]=='#':
                continue
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
            if season[0]=='#':
                continue
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
                if season[0]=='#':
                    continue
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

def derby():
    filename="derby.csv"
    multimp=[]
    mp=defaultdict(dict)
    x=filename.split(".")[0]
    buffer="const derby="
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0][0]=='#':
                continue
            derbyName=row[0]
            teams=row[1:]
            assert(len(teams)>=2)
            multimp.append((derbyName,teams))
    for (derby,teams) in multimp:
        for team in teams:
            if not(derby in mp[team]):
                mp[team][derby]=[]
            for otherteam in teams:
                if otherteam!=team:
                    mp[team][derby].append(otherteam)
    buffer+=json.dumps(mp)
    buffer+=";\n"
    return buffer

def foundation():
    filename="foundation.csv"
    mp={}
    buffer="const foundation="
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0][0]=='#':
                continue
            team=row[0]
            year=row[1]
            mp[team]=year
    buffer+=json.dumps(mp)
    buffer+=";\n"
    return buffer

if __name__ == '__main__':
    s=foundation()
    with open(FOUNDATION_OUTPUT,mode="w", encoding='utf-8') as f:
        f.write(s)

    s=derby()
    with open(DERBY_OUTPUT,mode="w", encoding='utf-8') as f:
        f.write(s)

    s=""
    s+=cnt('PL.txt')

    s+=title_list('UCL.csv')
    s+=title_list('UEL.csv')
    s+=title_list('CWC.txt')

    s+=final('FA.txt')
    s+=final('EFL.txt')
    s+=final('CWC.txt')
    s+=final('UCL.csv')
    s+=final('UEL.csv')

    s+=title('PL.txt')
    s+=title('UCL.csv')
    s+=title('UEL.csv')
    s+=title('FCWC.txt')

    s+=latest('APL.txt')
    s+=latest_all( "UCL.csv" ,"UEL.csv" ,"APL.txt","CWC.txt", "FCWC.txt","FA.txt", "EFL.txt"  )

    with open(OUTPUT,mode="w", encoding='utf-8') as f:
        f.write(s)
