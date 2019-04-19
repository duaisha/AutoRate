clear

for i in {1..5}

do echo $i

for filename in /mnt/isha/dataset/hams_dataset6_processed3/class$i/*.mp4
do
echo $filename

python2 remove_videos_less_10s.py -v $filename

done
done

