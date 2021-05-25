import json
import requests
url='http://api.openweathermap.org/data/2.5/weather?appid=4f8de2c0c02bdb9d3ba2eeb9fb8d0665&q='
city=input("please enter your city :")
newurl=url+city
Data=requests.get(newurl).json()
print(type(Data))
for i in Data:
    print(i)

print(Data['weather'])