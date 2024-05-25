import time
from plyer import  notification

time_seconds=float(input("Tell the seconds after which you want notification to drink water: "))
while(True):
    time.sleep(time_seconds)
    notification.notify(title="Drink water",
                        message="You should need to Drink water, Tanmay",
                        timeout=2)