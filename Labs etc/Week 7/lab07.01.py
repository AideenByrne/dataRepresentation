import requests
import json

url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=2019-11-10"
response = requests.get(url)
data = response.json()

listOfReports = []
#print(data)
for item in data["items"]:
    #print(item["ResourceName"])
    listOfReports.append(item["ResourceName"])


for ReportName in listOfReports:
    #print(ReportName)
    url = "https://reports.sem-o.com/api/v1/documents/"+ReportName
    print(url)
    response = requests.get(url)
    aReport = response.json()

filename = 'allreports.json'
f = open(filename, 'w')
json.dump(data, f, indent=4)

