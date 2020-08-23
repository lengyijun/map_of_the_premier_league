# 英超地图

![gif](screenshots/out.gif)

中国用户可以访问[这里](http://ggdg.gitee.io/map_of_the_premier_league/)


#### 介绍
1992-2019 英超地图(联赛,欧冠,欧联,足总杯,联赛杯,世俱杯,优胜者杯)

#### Feature
- 球队定位到球队当赛季的主场
- 当赛季的荣誉
- 截至该赛季的最后一个冠军
- 截至该赛季的最后一个联赛冠军
- 各项赛事的夺冠次数和年份
- 升降级信息
- 德比对手

#### How to use ?
![gif](screenshots/record.gif)


#### 缩写解释
| 简写 | 全称   |
| ---- | ---------------------------------- |
|UCL   | 欧冠      |
|UEL   | 欧联      |
|PL    | 英超      |
|FA    | 足总杯    |
|EFL   | 联赛杯    |
|APL   | 老英甲    |
|CWC   | 优胜者杯  |
|FCWC  | 世俱杯    |

#### 目录架构

```
├── csv/                  # origin csv file of js/ 
├── favicon.ico
├── screenshots/          # screenshots and gifs
├── img/
├── index.html
├── js/
├── locales/              # multi language support
├── map-style/            # map style. uesless for now
├── PLdata/               # every season Premier League data
├── README.md
└── README_zh.md
```



#### 安装教程

```
python3 -m http.server
```
Or use other static HTTP server, such as nginx or [see](https://github.com/wyhaya/see)

#### 更新数据
```
cd csv
./b.py

```

#### 生成gif
```
cd screenshots
convert -delay 120 -loop 0 *.png  out.gif
```
