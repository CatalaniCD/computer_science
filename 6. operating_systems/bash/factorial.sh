#!/bin/bash
number=1
while [ $number -le 6 ]          #Outer loop: Iterate from 1 to 6
do
        temp=$number
        factorial=1
        while [ $temp -ge 1 ]    #Inner loop: Iterate from N to 1
        do
                factorial=$(($factorial*$temp))
                temp=$(($temp-1))
        done
        echo "Factorial of $number = $factorial"
        number=$(($number+1))
done
