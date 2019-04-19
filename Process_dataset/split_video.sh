#!/bin/bash
clear

for i in {4..5}
do
echo $i
DIR_NAME="../hams_data_10sec/class"$i
end="$(find $DIR_NAME -type f | wc -l)"
start=1
echo $k
#echo $len
     for (( c=$start; c<=$end; c++ ))
        do
        echo $DIR_NAME"/trip"$c".mp4"
       python ffmpeg-split.py -f $DIR_NAME"/trip"$c".mp4" -s 10
       rm -rf $DIR_NAME"/trip"$c".mp4"
done
done

