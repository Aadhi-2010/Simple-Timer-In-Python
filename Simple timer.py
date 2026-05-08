import winsound
import time
a=int(input("Enter seconds to set timer:"))
b=0
while a!=b:
    print(a,"Seconds remaining")
    a-=1
    time.sleep(1)
print("Times Up!")
winsound.Beep(1000,500)