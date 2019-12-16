import requests, json
#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
#print(data)
#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
 json.dump(data, f, indent=4)
 
from xlwt import *
w = Workbook()
ws = w.add_sheet('githubusers')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"repos_url")
row += 1
for user in data["githubusers.json"]:
    ws.write(row,0, data["login"])
    ws.write(row,1,data["repos_url"])
    row += 1
w.save("githubusers.xls")