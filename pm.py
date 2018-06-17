import json
import urllib2

# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
#url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=python"

url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=52.39&longitude=16.89&historyHours=24"
apikey = "9658b2b3da0d45848fb1b312daccad29"
normPm10 = 50
normPM25 = 25
lcdRow = 4

lcdUrl = "http://192.168.1.200/control?cmd=lcd,"
request = urllib2.Request(url)
request.add_header("apikey", apikey)
response = urllib2.urlopen(request)



data = json.load(response)

# print the result
#print (data)

#print(data["currentMeasurements"])

aki =  data["currentMeasurements"]["airQualityIndex"]
pm25 =  data["currentMeasurements"]["pm25"]
pm10 = data["currentMeasurements"]["pm10"]


#print (aki)
#print(pm25)
#print(pm10Percentage)

ergebnis = 'PM10:{:.0%} PM25:{:.0%}'.format(pm10/normPm10,pm25/normPM25)
print (ergebnis)

from lcdbridge import LCDBridge

lcd = LCDBridge()

lcd.send2LCD(4, 1, ergebnis)


