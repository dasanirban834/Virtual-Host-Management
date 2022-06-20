#!/bin/bash

#jq . reboot.json | jq .Servers[0]
#jq . reboot.json | jq .Servers[1]
len=$(jq . reboot.json | jq '.Servers | length')
#echo $len
i=0
while [[ i -lt $len ]]
do
        echo "Index is : " $i
        aws ec2 reboot-instances --instance-ids $(jq . reboot.json | jq .Servers[$i] | sed 's/"//g')
        ((i++))
done
