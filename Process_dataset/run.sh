clear

DIR_NAME="videos/trip1/"
video_name="trip1.mp4"
mkdir $DIR_NAME

cp -r $video_name $DIR_NAME

python2 ffmpeg-split.py -f "$DIR_NAME""$video_name" -s 10
rm -rf "$DIR_NAME""$video_name" 

for trip in "$DIR_NAME"*
       do
	trip_dummy=trip_dummy.mp4
        cp -r $trip $trip_dummy
        ffmpeg -i $trip -strict -2  -vf "transpose=1" $trip_dummy -y
	cp -r $trip_dummy $trip
       	ffmpeg -i $trip_dummy -strict -2 -vf "transpose =3" $trip -y
	

