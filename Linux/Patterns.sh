#!/bin/bash

filename="$1"
tofilename="$2"

#method(int i) method ( int i )
sed -e 's/(\(.*\)/( \1/g' -e 's/\(.*\))/\1 )/g' "$filename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"
sed 's/(  )/()/g' "$tofilename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"

#multiply(BigInteger val) multiply (BigInteger val)
sed -e 's/\(.*\)(\(.*\))/\1 (\2)/g' -e 's/}\([^ ]*\)/} \1/g' -e 's/\([^ ]*\){/\1 {/g' "$tofilename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"
sed 's/\([^ ]*\) ()/\1()/g' "$tofilename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"
sed 's/\(.*\)  {/\1 {/g' "$tofilename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"
sed 's/} $/}/g' "$tofilename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"

#=><-
#NOT WORKING
sed 's/(\([a-z0-9]*\)\([+-=><]*\)\([a-z0-9]*\))/(\1 \2 \3)/g' "$tofilename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"

#array[i] array[ i ]
#sed 's/[\(?*\)/[ \1/g' "$filename" > "$tofilename"
#sed 's/\(?*\)]/\1 ]/g' "$filename" > "$tofilename"

#Tab to space
sed 's/\t/    /g' "$tofilename" >  index.txt.tmp && mv index.txt.tmp "$tofilename"
