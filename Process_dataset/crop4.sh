
#####################  Part2 : Crop videos ##########################3

for j in {1..1}
do
echo $j
DIR_NAME2="../hams_dataset61_processed/class"$j
OUT_NAME2="../hams_dataset61_processed2/class"$j


for trip in "$DIR_NAME2"/*
       do
        trip2="${trip/processed/processed2}"
        trip3="${trip/processed/processed3}"
	trip_temp1="${trip/processed/processed4}"
   	trip_temp2="${trip/processed/processed5}"




        echo $trip2
	echo "################################################################################################"
	echo $trip_temp2
        echo "##############################################################################################"
	
	sudo ffmpeg -i $trip -strict -2  -vf "transpose=1" $trip_temp1 -y
	sudo ffmpeg -i $trip_temp1 -strict -2 -vf "transpose =3" $trip_temp2 -y



        array=()
        while read line;
        do
        array+=($line)
        done< <(sudo python2 preprocess.py -p  "shape_predictor_68_face_landmarks.dat" -v "$trip_temp2")

        echo ${array[@]}

        x=${array[0]}
        y=${array[1]}

        echo $x
        echo $y

        sudo ffmpeg -i $trip_temp2 -strict -2 -filter:v "crop=1500:1080:$x:$y" $trip2 -y
	echo "yup"

	if [ ! -f $trip3 ]; then
	  echo "File not found!"

        sudo ffmpeg -i "$trip2"  -r 5 -s 500x500 -c:v libx264 -b:v 3M -strict -2 -movflags faststart "$trip3" -y
	fi 

 done

done

