import requests
import smtplib
import sys

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

url = 'https://one.ufl.edu/apix/soc/schedule/?category=RES&term=2241&course-code=cap4053'


EMAIL = 'arangodonny@gmail.com'
PASSWORD = 'phvg ftiq svrg amrg' 


response = requests.get(url).json()
waitlist = response[0]['COURSES'][0]['sections'][0]['waitList']
print(waitlist)

def getWaitList():
    response = requests.get(url).json()
    waitList = response[0]['COURSES'][0]['sections'][0]['waitList']
    print(waitlist)
    return waitList

def notifyWaitList(waitList, phone_number, carrier, message):
    if(waitlist['isEligible'] != 'N'):
       send_message(phone_number, carrier, message)

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    email = f"Subject:WaitList Open\nTo:{recipient}\n{message}"
    server.sendmail(auth[0], recipient, email)

def send_email(recipient, message):
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    email = f"Subject:WaitList Open\nTo:{recipient}\n{message}"
    server.sendmail(auth[0], recipient, email)
 
 
if __name__ == "__main__":
    # if len(sys.argv) < 4:
    #     print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
    #     sys.exit(0)
 
    #phone_number = sys.argv[1]
    #carrier = sys.argv[2]
    recipient = sys.argv[1]
    message = sys.argv[2]
 
    #send_message(phone_number, carrier, message)
    send_email(recipient, message)