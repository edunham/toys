# "It's Twosday!"

# Let's say a "Twosday" is a Tuesday the 22nd.
# When will they be?


for m in $(seq 1 12)
do

    for y in $(seq 2016 2030)
    do
        DATE="$y-$m-22"
        WEEKDAY=$(date -d "$DATE" +%a )
        case $WEEKDAY in
            "Tue")
                echo $DATE;;
        esac
    done
done
