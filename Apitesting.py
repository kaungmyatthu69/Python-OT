#key="af7559aa804480794809a7ed4a92948f0"
import json
import requests
url='http://api.openweathermap.org/data/2.5/weather?appid=4f8de2c0c02bdb9d3ba2eeb9fb8d0665&q='
city=input("please enter your city :")
newurl=url+city
Data=requests.get(newurl).json()
print(type(Data))
JsonData=json.dumps(Data,indent=4)
print(JsonData)
print(type(JsonData))