#!/usr/bin/python3
import csv
import copy

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
def title(filename):
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
            year=season.split("-")[0]
            if(int(year)>=1992):
                res[season]=data
    print(res,end="")
    print(";")

if __name__ == '__main__':
    cnt('PL.txt')

    title('UCL.txt')
    title('UEL.txt')
    title('CWC.txt')

    final('FA.txt')
    final('EFL.txt')
