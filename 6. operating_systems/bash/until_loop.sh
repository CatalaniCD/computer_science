#!/bin/sh
read number
counter=1
until [ $counter -gt 10 ]
do
   multiply=$(($number*$counter))
   echo "$number x $counter = $multiply"
   counter=$(($counter+1))
done
