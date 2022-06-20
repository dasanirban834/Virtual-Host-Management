#!/bin/bash
jq . reboot.json
h=$(jq . reboot.json | jq .Servers)
echo $h
for i in ${#h[@]}
do
        aws ec2 reboot-instances --instance-ids ${h[$i]}
        i=i+1
done
