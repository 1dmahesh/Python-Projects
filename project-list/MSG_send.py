
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

schedule.every(10).seconds.do(msg_send)
#msg_send

while True:
    schedule.run_pending()
    time.sleep(1)