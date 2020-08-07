#!/usr/bin/python3
import csv
import copy

def title(filename):
    mp={}
    res={}
    x=filename.split(".")[0]
    print("const "+x+"_list=")
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


if __name__ == '__main__':
    title('UCL.txt')
    title('UEL.txt')
    title('CWC.txt')
