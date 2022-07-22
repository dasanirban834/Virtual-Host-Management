#!/bin/bash

#jq . stop.json | jq .Servers[0]
#jq . stop.json | jq .Servers[1]
len=$(jq . stop.json | jq '.Servers | length')
#echo $len
i=0
while [[ i -lt $len ]]
do
        echo "Index is : " $i
        aws ec2 stop-instances --instance-ids $(jq . stop.json | jq .Servers[$i] | sed 's/"//g')
        ((i++))
done
