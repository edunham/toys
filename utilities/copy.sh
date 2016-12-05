# With NFS stuff mounted to /mnt and a local list of directories `music.txt`,
# get the stuff in the list.

while read FILE
do
    FILESIZE=$(du -sh "/mnt/Music/$FILE" | cut -d'/' -f1)
    if [[ $FILESIZE == *G* ]]
    then
        echo "$FILESIZE $FILE" >> test.txt
    else
        echo -e " \t $FILE is $FILESIZE"
        #cp -r /mnt/Music/"$FILE" /home/edunham/Music/
    fi

done < music.txt
