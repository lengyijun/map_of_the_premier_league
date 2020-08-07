set -e
set -u

for i in {1..27}; do
  url=`printf 'https://footballapi.pulselive.com/football/standings?compSeasons=%s&altIds=true&detail=2&FOOTBALL_COMPETITION=1' "$i"`
  filename=`printf '%s-%s.json' "$((i+1991))" "$((i+1992))"`
  # echo $url
  # echo $filename

  curl $url \
    -H 'authority: footballapi.pulselive.com' \
    -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' \
    -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
    -H 'accept: */*' \
    -H 'origin: https://www.premierleague.com' \
    -H 'sec-fetch-site: cross-site' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-dest: empty' \
    -H 'referer: https://www.premierleague.com/tables?co=1&se=18&ha=-1' \
    -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8' \
    --compressed   > $filename
   
done

# curl 'https://footballapi.pulselive.com/football/standings?compSeasons="%i"&altIds=true&detail=2&FOOTBALL_COMPETITION=1' \
  # -H 'authority: footballapi.pulselive.com' \
  # -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' \
  # -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  # -H 'accept: */*' \
  # -H 'origin: https://www.premierleague.com' \
  # -H 'sec-fetch-site: cross-site' \
  # -H 'sec-fetch-mode: cors' \
  # -H 'sec-fetch-dest: empty' \
  # -H 'referer: https://www.premierleague.com/tables?co=1&se=18&ha=-1' \
  # -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8' \
  # --compressed   >18.json

