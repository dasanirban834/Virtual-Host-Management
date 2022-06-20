#!/bin/bash

#jq . start.json | jq .Servers[0]
#jq . start.json | jq .Servers[1]
len=$(jq . start.json | jq '.Servers | length')
#echo $len
i=0
while [[ i -lt $len ]]
do
        echo "Index is : " $i
        aws ec2 start-instances --instance-ids $(jq . start.json | jq .Servers[$i] | sed 's/"//g')
        ((i++))
done
