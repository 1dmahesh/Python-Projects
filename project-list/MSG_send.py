#This program can be used for sending schedule SMS for user.
# For this to run we need to provide mobile number in credentials.py file
# Please don't spam strangers, inspite you can freack your friends with this.
from credentials import mobile_number
import requests
import schedule
import time

def msg_send():
    resp = requests.post('https://textbelt.com/text',{
        'phone': mobile_number,
        'message': 'Hey, bro This is a Text Message',
        'key' : 'textbelt'
})
    print(resp.json())

#currently this will send msg in every 10 seconds, you can configure it by you likes.
schedule.every(10).seconds.do(msg_send)

#msg_send
while True:
    schedule.run_pending()
    time.sleep(1)