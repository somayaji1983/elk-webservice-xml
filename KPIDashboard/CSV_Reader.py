# importing csv module
import csv
import calendar
import datetime as dt
import json
import requests

# csv file name
filename = "/Users/ramesh.dhavala/projects/KPIDashboard/KPI_Dashboard_sample.csv"

# initializing the titles and rows list
resplist = []

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	
	# extracting each data row one by one
	for row in csvreader:
		responseitem = {}
		responseitem.__setitem__('logdate',row[0])
		datestr=dt.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S")
		responseitem.__setitem__('count',row[1])
		responseitem.__setitem__('hour',datestr.hour)
		responseitem.__setitem__('weekday',calendar.day_name[datestr.weekday()])
		responseitem.__setitem__('month',calendar.month_name[datestr.month])
		resplist.append(responseitem)
	

# get total number of rows
finalobj = {}
finalobj.__setitem__("result",resplist)
jsondata=json.dumps(finalobj)

print jsondata

#headers = {"Content-Type": "application/json"}
#url="http://127.0.0.1:9200/kpidashboard"
#loadrsp = requests.put(url,data=jsondata,headers=headers)
#print(loadrsp)