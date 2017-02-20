#!/bin/bash
#This is a calulator
res="No result"

	case $1 in
		add) res=$(($2 + $3));;
		sub) res=$(($2 - $3));;
		mult) res=$(($2 * $3));;
		div) val=$(($2 / $3));;
		?) echo "Option not allowed $1";;
	esac

echo $res
