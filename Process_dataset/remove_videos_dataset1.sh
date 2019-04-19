clear

for filename in /mnt/isha/dataset/hams_dataset1_processed3/testing_ordered/*.mp4
do
echo $filename

python2 remove_videos_less_10s.py -v $filename

done
