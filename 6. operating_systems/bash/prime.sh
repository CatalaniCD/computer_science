#!/bin/sh
# detect if a number is prime by checking the remainder, %, between 2 and number/2
read number
counter=2
flag=0
if [ $number -eq 0 -o $number -eq 1 ]
then
        flag=1
else
        while [ $counter -le $(($number/2)) ]
        do
                if [ $(($number%$counter)) -eq 0 ]
                then
                        flag=1
                        continue
                fi
                counter=$(($counter+1))
        done
fi

if [ $flag -eq 0 ]
then
        echo "$number : is a prime number"
else
        echo  "$number : is not a prime number"
fi
