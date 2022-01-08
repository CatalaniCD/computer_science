#!/bin/bash
isEven()
{
	if [ $(($1%2)) -eq 0 ]
	then
		return 0
	else
		return 1
	fi
}
read num
if isEven num
then
	echo "$num is an even number"
else
	echo "$num is an odd number"
fi
