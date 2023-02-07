import pywhatkit as pyw
import datetime

user = input("Enter Your Message")
number = input("Enter Number with +country code")

now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1
print(minute)

pyw.sendwhatmsg(f"{number}", f"{user}", hour, minute)

print("Message Sent Successfully")
