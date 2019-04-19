#!/bin/bash


for i in {1..5}
do
echo $i
DIR_NAME="../hams_dataset6/class"$i
OUT_NAME="../hams_dataset61_processed/class"$i

end="$(find $DIR_NAME -type f | wc -l)"
start=1

for (( c=$start; c<= end; c++ ))
	do
        echo "##############################################################################################"
        #echo $DIR_NAME"/trip"$c".mp4"
        input_video=$DIR_NAME"/trip"$c".mp4"
      	output_video=$OUT_NAME"/trip"$c".mp4"

      	echo "$input_video"
      	echo "$output_video"

        sudo python2 ffmpeg-split.py -f "$output_video" -s 10
        sudo rm -rf "$output_video"
      done

done
echo "all done"

#####################  Part2 : Crop videos ##########################3

#for j in {1..5}
#do
#echo $j
#DIR_NAME2="../hams_dataset2_processed/class"$j
#OUT_NAME2="../hams_dataset2_processed2/class"$j


#for trip in "$DIR_NAME2"/*
#	do
 #       trip2="${trip/processed/processed2}"
  #      trip3="${trip/processed/processed3}"
 #       echo $trip2
   #     echo "##############################################################################################"

    #    array=()
     #   while read line;
     #   do
      #  array+=($line)
     # done< <(python2 preprocess.py -p  "shape_predictor_68_face_landmarks.dat" -v "$trip")

 #       echo ${array[@]}
#
  #      x=${array[0]}
   #     y=${array[1]}

    #      echo $x
     #   echo $y

      #  ffmpeg -i "$trip" -strict -2 -filter:v "crop=1500:1080:$x:$y" "$trip2" -y
       # ffmpeg -i "$trip2"  -r 5 -s 500x500 -c:v libx264 -b:v 3M -strict -2 -movflags faststart "$trip3" -y
 # done

#done
