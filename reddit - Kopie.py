import requests
import requests.auth
import json
 
client_auth = requests.auth.HTTPBasicAuth('notMyClient', 'notMySecret')
post_data = {"grant_type": "password", "username": "notMyUserName", "password": "notMyPassword"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}

response = requests.post("https://www.reddit.com/r/de/top.json", auth=client_auth, data=post_data, headers=headers)
response2 = requests.post("https://www.reddit.com/r/france/top.json", auth=client_auth, data=post_data, headers=headers)
response3 = requests.post("https://www.reddit.com/r/Austria/top.json",auth=client_auth, data=post_data, headers=headers)

de = response.json()
fr = response2.json()
au = response3.json()

print(de)


with open("Top_DE.json","w") as json_output:
	json.dump(de, json_output)	
	
with open("Top_FR.json","w") as json_output:
	json.dump(fr, json_output)	
with open("Top_AU.json","w") as json_output:
	json.dump(au, json_output)		
