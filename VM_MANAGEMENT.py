#print("Virtual Host Management Catalog")
#import time
#import sys
import requests
import json

# Repository File API link
url_start = "https://gitlab.com/api/v4/projects/<project-id>/repository/files/start%2Ejson?ref=main"
url_reboot = "https://gitlab.com/api/v4/projects/<project-id>/repository/files/reboot%2Ejson?ref=main"
url_stop = "https://gitlab.com/api/v4/projects/<project-id>/repository/files/stop%2Ejson?ref=main"

# provide servers instance ids
server_list = list(input("Please enter the server names : ").split(" "))
print("The list of server : ", server_list)

# servers instance ids in the form of JSON
payload = json.dumps({"branch": "main", "commit_message": "update file", "content": json.dumps({"Servers": server_list}, indent=4)})

# provide content type and bearer token/gitlab API token
headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer glpat-xxxxxxxxxxxxxx'
}

# Create choices 1: start, 2: reboot, 3: stop
option1 = {"1":"Start", "2": "Reboot", "3": "Stop"}
v = input('''Please select the action from above : 
1. Start
2. Reboot
3. Stop
Default [1] : ''')

# Making logics based upon the user choice
if v == "1":
   print("You have chosen : ", option1["1"])
   response_start = requests.request("PUT", url_start, headers=headers, data=payload)
   print(response_start)
elif v == "2":
   print("You have chosen : ", option1["2"])
   response_reboot = requests.request("PUT", url_reboot, headers=headers, data=payload)
   print(response_reboot)
elif v == "3":
   print("You have chosen : ", option1["3"])
   response_stop = requests.request("PUT", url_stop, headers=headers, data=payload)
   print(response_stop)
else:
   print("Not Required")
