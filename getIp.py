import csv
import requests
import time

url = "https://api.ipify.org/?format=json"

def getIp():
    r1 = requests.get(url)
    ip = r1.json()
    return ip
time = time.asctime()
#print(time)

ip = getIp()
print(time +' = ' + ip['ip'])
