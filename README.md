# vaccine-india
Find vaccination centers with available vaccine dose. Create notification for vaccine availability in your mobile

#requirements 
This file is for termux. To run this file you will need -
1. Termux-APL
2. Python libraries
2.1. requests
2.2. date time
2.3. json
2.4. os
2.5. time

#edits/changes
You can change following variables to change output
1. Change variable 'al' to change beneficiary age eg. 18, 45
2. Change variable 'district' to change your district. District values are in form of codes. Code 503 is for kota, rajasthan. To find your state code visit https://cdn-api.co-vin.in/api/v2/admin/location/states . To find your district code change state_code to your state and visit https://cdn-api.co-vin.in/api/v2/admin/location/districts/state_code
3. This code check vaccine availability after every 60 sec. If you want to change it change time.sleep() value. But be careful api request must not exceed 100requesta/5 min value. 
4. If you want to change content of notification or toast change it as per termux-api guide 
5. If you want to use this code in PC or Laptop use vaccine_pc.py 
