for dir in /home/edunham/repos/*
do
    cd $dir
    day=$(git log -1 --format="%ci")
    echo "${day}, ${dir}"
    cd ..
done

#I'm better as ./latest-commits.sh | sort -t, -nk1

