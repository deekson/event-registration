import os
import smtplib

def registration():
	
	os.system('clear')
	newname = input("Enter name: ")
	newemail = input("Enter email: ")
	contactlist[newname] = newemail
	print("Success!")

	
def printout():
	os.system('clear')

	name = input("Enter registrants name: ")
	if name in contactlist.keys():
		print ("Name: {} \nEmail: {}".format(name,contactlist[name]))
	else:
		print ("{} has not yet been registered".format(name))


def sendemail():
	os.system('clear')

	name = input("Search contact to email: ")
	if name in contactlist.keys():
		confirm = input("Do you want to send {} an email? Yes/No: ".format(name))
		if confirm == "Yes":
			print ("Sending Email...")
			msg = "Hello {}, you have been invited to attend Accra's hottest networking event. Kindly confirm your email is {}".format(name,contactlist[name])
			emailid = contactlist[name]
			sendmail(emailid,msg)
		else:
			print("Exiting...")
	else:
		print ("{} is not in the maillist".format(name))


def sendmail(emailid,msg):
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("xxx@gmail.com", "")
	server.sendmail("xxx@gmail.com", emailid,msg)
	server.quit()

def menu():
	print()
	print("1. New Registration \n")
	print("2. Get registration details \n")
	print("3. Send Email \n")
	print("4. Quit \n")
	return input("Type corresponding digit and press Enter \n")


contactlist = {}
choice = menu()

while choice != "4":

    if choice == "1":
    	registration()

    elif choice == "2":
        printout()

    elif choice == "3":
        sendemail()

    else:
    	print("Invalid Choice")

    choice = menu()