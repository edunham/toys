#!/bin/bash

begin=$(date -I -d "2012-02-01")
end=$(date -I -d "2017-07-01") # should automatically be first day of next month

while [[ "$begin" < "$end" ]]; do
    temp=$(date -I -d "$begin + 1 month")
    n=$(git log --author="bors-servo" --pretty=format:"%cd  %h  %s" --before={$temp} --after={$begin} | wc -l)
    echo $n , $begin
    begin=$temp
done
