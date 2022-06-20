#print("Virtual Host Management Catalog")
#import time
#import sys
import requests
import json

url_start = "https://gitlab.com/api/v4/projects/36759585/repository/files/start%2Ejson?ref=main"
url_reboot = "https://gitlab.com/api/v4/projects/36759585/repository/files/reboot%2Ejson?ref=main"
url_stop = "https://gitlab.com/api/v4/projects/36759585/repository/files/stop%2Ejson?ref=main"

server_list = list(input("Please enter the server names : ").split(" "))
print("The list of server : ", server_list)
payload = json.dumps({"branch": "main", "commit_message": "update file", "content": json.dumps({"Servers": server_list}, indent=4)})
headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer glpat-Q3HTF8tjxJJkcLzDo_zX'
}

option1 = {"1":"Start", "2": "Reboot", "3": "Stop"}
v = input('''Please select the action from above : 
1. Start
2. Reboot
3. Stop
Default [1] : ''')
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