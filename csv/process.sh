#!/usr/bin/env bash
set -e
set -u
# set -x

OUTPUT=../js/autogenerate.js
rm -f $OUTPUT

latest(){
  filename="$1.txt"
  x=$1
  awk '
  BEGIN{ FS=","
  printf("const %s_%s=\{","'$x'","'${FUNCNAME[0]}'") }
  {
    map[$2]=$1
      if($1>=1992){
        printf("\"%s\":\{",$1)
        for (var in map){
          printf("\"%s\":\"%s\",",var,map[var])
        }
      print "\},"
}
}
END{ print "\};" }
' "$filename" | sed 's/,}/}/g'  >> $OUTPUT

echo >> $OUTPUT
}

latest_all(){
  x=all
  awk '
  BEGIN{ FS="," }
  {
    if($1>=year[$2]){
      year[$2]=$1
      title[$2]=FILENAME
    }
  }
END{ 
  printf("const %s_%s=\{","'$x'","'${FUNCNAME[0]}'") 
  for (var in year){
    printf("\"%s\":\{year:\"%s\",",var,year[var])
    printf("title:\"%s\",",title[var])
    printf "\},"
  }
  print "\};" 
}
' "$@" | 
  sed 's/,}/}/g'  |
  sed 's/APL.txt/Premier League/g' |
  sed 's/UCL.txt/UEFA Champion League/g' |
  sed 's/UEL.txt/UEFA Europa League/g'   |
  sed 's/FA.txt/Football Association Challenge Cup/g' |
  sed 's/EFL.txt/English Football League Cup/g' |
  sed 's/FCWC.txt/FIFA Club World Cup/g' >> $OUTPUT

echo >> $OUTPUT
}


#use python script instead
# cnt UCL
# cnt UEL

# cnt PL
# cnt FA

# latest APL

# title PL
# title UCL
# title UEL
# title FA
# title EFL
# title FCWC
# title CWC

latest_all UCL.txt UEL.txt FA.txt EFL.txt FCWC.txt APL.txt CWC.txt

python3 b.py >> $OUTPUT
