import os
import time
import requests
from twilio.rest import Client

url = 'https://one.ufl.edu/apix/soc/schedule/?category=RES&term=2241&course-code=cap4053'

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_message(classCode):
    message = client.messages \
    .create(
        body=f"{classCode} HAS A WAITLIST SPOT AVAILABLE!",
        from_='+18557860335',
        to='+17274656012'
    )

def getWaitList():
    response = requests.get(url).json()
    waitList = response[0]['COURSES'][0]['sections'][0]['waitList']
    classCode = response[0]['COURSES'][0]['code']
    return classCode, waitList

def notifyWaitList():
    classCode, waitList = getWaitList()

    if(waitList['isEligible'] != 'N'):
       send_message(classCode)
       exit()
    else:
        print('waitList Full')

def main():
    while True:
        notifyWaitList()
        time.sleep(60)

if __name__ == "__main__":
    main()



    