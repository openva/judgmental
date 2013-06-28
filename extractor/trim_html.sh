#! /bin/bash
for i in *
do
	if [[ $i =~ ".html" ]];
	then
		sed -n '/<BODY>/,$p' $i | tail -n +2 | head -n -2 | sed 's/&#160;/ /g' > $i
	fi
done