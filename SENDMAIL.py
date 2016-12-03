import smtplib

fromemail = 'XXXX'

# Gmail Login
username = 'XXXX'
password = 'XXXX'

#gmail login
print("Try to login...")
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
print("Login Success.")

#read message from file.
filemsg = open("message.txt","r")
message=''
for line in filemsg:
	message += line
filemsg.close()

print("Message : \n",message)

#read Email address from file (line by line)
counter=0
file = open("input.txt","r")
for email in file:
	# Sending the mail  	
	server.sendmail(fromemail,email, message)
	print("Email Sent to ",email)
	counter+=1;
file.close()
print("Total Email Sent : ",counter);
server.quit()
