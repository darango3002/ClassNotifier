import os
import time
import sys
from dotenv import load_dotenv
import requests
import http.client, urllib.parse
from pushover import Pushover
from datetime import datetime

url = 'https://one.ufl.edu/apix/soc/schedule/?category=RES&term=2241&course-code=cap4053'

load_dotenv()
app_token = os.environ.get('APP_TOKEN')
user_key = os.environ.get('USER_KEY')

po = Pushover(app_token)
po.user(user_key)

def send_message(classCode):
    msg = po.msg(f"Wailist position in {classCode} has opened up")
    msg.set("title", "Class Notifier")
    msg.set("priority", "1")
    po.send(msg)
    sys.exit("Message Sent")

def getWaitList():
    response = requests.get(url).json()
    waitList = response[0]['COURSES'][0]['sections'][0]['waitList']
    classCode = response[0]['COURSES'][0]['code']
    return classCode, waitList

def notifyWaitList():
    classCode, waitList = getWaitList()

    if(waitList['isEligible'] != 'N'):
       send_message(classCode)
    else:
        print(f'waitList Full at {datetime.now().strftime("%H:%M:%S")}')

def main():
    while True:
        notifyWaitList()
        time.sleep(60)

if __name__ == "__main__":
    main()



    