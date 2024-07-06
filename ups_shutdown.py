# import requests module 
import requests 
import json
import os

from urllib3.exceptions import InsecureRequestWarning
 
# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Making a get request 
# Change IP address to your IP address
response = requests.get('https://ipaddress:8210/api/PowerAssist', verify=False) 

#print(response.json()[0])

requests.packages.urllib3.disable_warnings()


isDischarging = response.json()[0]["status"]["isDischarging"]
needsReplacement = response.json()[0]["status"]["needsReplacement"]
isInternalFailure = response.json()[0]["status"]["isInternalFailure"]

# response = json.dumps(response.json(), indent=4, sort_keys=True)

if isDischarging:
    os.system("shutdown now -h")
