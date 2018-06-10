import time
import os
import webbrowser
import urllib
x='''
	press 1 for current date and time
	press 2 to create a file
	press 3 to create a directory
	press 4 to search something on google
	press 5 to shutdown your system
	press 6 to check internet connectio in pc
	press 7 to get the list of ip on network
	press 8 to reboot your system
	press 9 to logout your system
  '''
print (x)

choice = raw_input("enter your choice")

if choice == '1':
	print ("your current date and time is ....")
	print (time.ctime())

elif choice == '2':
	name = raw_input("enter the name of file:")
	with open(name,"w") as name:
	 name.write();

elif choice == '3':
	name = raw_input("enter the name of directory")
	os.makedirs(name)

elif choice == '4':
	msg = raw_input("type text you want to search")
	webbrowser.open_new_tab("https://www.google.com/seach?q="+msg)

elif choice == '5':
	check = raw_input("are you sure y/n")
	if check == 'n':
		exit()
	else: 
		os.system("shutdown -s -t 1")

elif choice == '6' :	
	urllib.urlopen("https://www.google.com/")
	
elif choice == '7' :
	ip_adr = raw_input("enter the ip of network ")
	os.system("nmap -sn " + ip_adr)
	
elif choice == '8':
	check = raw_input("are you sure y/n")
	if check == 'n':
		exit()
	else: 
		os.system("shutdown -r -t 1")
	
elif choice == '9':
	check = raw_input("are you sure y/n")
	if check == 'n':
		exit()
	else: 
		os.system("pkill -KILL -u username")	
		
else:
	print("wrong option")	 

