import requests
import  json
from datetime import datetime
import os
import time

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

al = 18  #age limit
district = '503'  #district_code

date = datetime.today().strftime('%d-%m-%Y') #date
avl = 'available_capacity'
age = 'min_age_limit'


url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+district+"&date="+date

while(1):
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	#print(response.status_code)
	#print(url)
	data = response.json()

	alert =''
	i=0
	x = len(data['centers'])
	centers = data['centers']
	vaccine = 0
	while(i<x) :
		j=0
		y = len(centers[i]['sessions'])
		sessions = centers[i]['sessions']
		while(j<y) :
			if sessions[j][avl] != 0 and sessions[j][age] == al :
				alert = alert + str(sessions[j][avl]) +'doses \t'+ str(centers[i]['name']) +'\t'+ str(centers[i]['pincode']) +'\t' + str(centers[i]['fee_type'])+'\n'
				vaccine+=1
			j+=1
		i+=1

	alert = "Vaccine for "+str(al)+"+ available at "+str(vaccine)+" places.\n\n"+alert
	if vaccine>0 :
		sound = " --sound"
		os.system("termux-toast -g top Vaccine available")
		print(datetime.today())
		print(alert)
	else :
		sound  = ""
	command = "termux-notification -i 313933 -c \"" + alert + "\" -t 'Vaccine Alert'"+sound
	os.system(command)
	time.sleep(60)
