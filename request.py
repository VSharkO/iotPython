
import serial, string, time
import requests
import json

flag = 0
flagReq = 0
output = " "
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
status = "none"
message = "none"
while True:
	output = ser.readline()
	if output == "":
		flag = 0
		flagReq = 0
	if output >= "0" and output <= "9":
		if flag == 0:
			flag = 1
			statusRequest = requests.get('https://boiling-bastion-42729.herokuapp.com/api/v1/statuses')
			sare = statusRequest.json()
			status = sare[0]['isActive']
		if status == 't':
			if flagReq == 0:
				flagReq = 1
				deviceReq = requests.get('https://boiling-bastion-42729.herokuapp.com/api/v1/devices/'+output)
				req = deviceReq.json()
				message = req['message']
				print(message)
		
