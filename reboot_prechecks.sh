#!/bin/bash
server_list=$(jq . reboot.json | jq .Servers)
for j in ${#server_list[@]}
do
        aws ec2 describe-instances --instance-id $(server_list[i]) --query "Reservations[*].Instances[*].{PrivateIP:PrivateIpAddress,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}" --output table
        j=j+1
done