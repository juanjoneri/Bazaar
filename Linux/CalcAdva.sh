#!/bin/bash
#This is a calulator that performs multiple operations
#Example:
#$ 6 add 9 sub 1 div 2 mylt 3
#$ 21
result=0
op=init

for var in "$@"
do
    case $op in
        init)result=$var;echo "= $var";;
        a)result=$(($result + $var )); echo "+ $var = $result";;
        s)result=$(($result - $var));echo "- $var = $result";;
        m)result=$(($result * $var));echo "* $var = $result";;
        d)result=$(($result / $var));echo "/ $var = $result";;
    esac

    case $var in
		add) op=a;;
		sub) op=s;;
		mult) op=m;;
		div) op=d;;
        *) op="other";;
	esac
done
