import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
if(timestamp>'05:00:00' and timestamp<'12:00:00'):
    print("Good morning....")
elif(timestamp>='12:00:00' and timestamp<'16:00:00'):
    print("Good afternoon....")
elif(timestamp>='16:00:00' and timestamp<'20:00:00'):
    print("Good Evening....")
elif(timestamp>='20:00:00' and timestamp<'00:00:00'):
    print("Good Night....")
else:
    print("Raat ho rhi kuch greeting nhi milegi soja")




