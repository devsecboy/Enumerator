#!/bin/sh
if [ $# -lt 1 ];then
  echo "$0 <wordlist>" && exit 1
fi
echo "Cleaning $1"
cp $1 $1.old
sort -d $1 | uniq > $1.new
mv $1.new $1
printf "Number of words: %s\n" `wc -l $1|awk '{print $1}'`

