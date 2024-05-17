from shoshalmedia.socialmedia import send_message
import re
Data =" send message to kiran kumar"
pattern ="send message to (\D*)"
matchs = re.findall(pattern,Data)
to = matchs
print(to)
#print("what's the messege sir")
#Data = input("")
#message = Data
#Reply = send_message(to, message)