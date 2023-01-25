#! /bin/bash 
H=$(date +%H)
M=$(date +%M)
if (( 6 <= 10#$H && 10#$H <= 10 )) || (( 10#$H == 23 )); then
  echo "batch server is busy. try again a few minute later"
  exit 1
else
  if (( 10 <= 10#$M && 10#$M <= 15 )) || (( 40 <= 10#$M && 10#$M <= 45 )); then
    echo "batch server is busy. try again a few minute later"
    exit 1
  fi
fi