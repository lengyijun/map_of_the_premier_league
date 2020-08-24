#!/usr/bin/env bash

split() {
   # Usage: split "string" "delimiter"
   IFS=$'\n' read -d "" -ra arr <<< "${1//$2/$'\n'}"
   printf '%s\n' "${arr[@]}"
}

promotion() {
  printf '"%s"' $(split "$2" "."  | head -n 1)
  echo ':['
  diff <(jq '.tables[0].entries |  map(.team.name) | .[]' < "$1" | sort ) <(jq '.tables[0].entries |  map(.team.name) | .[]' < "$2" | sort ) | grep "^>" | sed  's/^..//'  | xargs -I{} printf '"%s",' {}
  echo '],'
}

echo 'const promotion={"1992-93":["Ipswich Town","Middlesbrough","Blackburn Rovers"],'
promotion 1992-93.json   1993-94.json
promotion 1993-94.json   1994-95.json
promotion 1994-95.json   1995-96.json
promotion 1995-96.json   1996-97.json
promotion 1996-97.json   1997-98.json
promotion 1997-98.json   1998-99.json
promotion 1998-99.json   1999-2000.json
promotion 1999-2000.json 2000-01.json
promotion 2000-01.json   2001-02.json
promotion 2001-02.json   2002-03.json
promotion 2002-03.json   2003-04.json
promotion 2003-04.json   2004-05.json
promotion 2004-05.json   2005-06.json
promotion 2005-06.json   2006-07.json
promotion 2006-07.json   2007-08.json
promotion 2007-08.json   2008-09.json
promotion 2008-09.json   2009-10.json
promotion 2009-10.json   2010-11.json
promotion 2010-11.json   2011-12.json
promotion 2011-12.json   2012-13.json
promotion 2012-13.json   2013-14.json
promotion 2013-14.json   2014-15.json
promotion 2014-15.json   2015-16.json
promotion 2015-16.json   2016-17.json
promotion 2016-17.json   2017-18.json
promotion 2017-18.json   2018-19.json
promotion 2018-19.json   2019-20.json
promotion 2019-20.json   2020-21.json
echo '};'
