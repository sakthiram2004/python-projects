from datetime import *
print("Enter DOB")
y=int(input("Enter YYYY"))
m=int(input("Enter m"))
d=int(input("Enter d"))
dob=date(y,m,d)
cd=date.today()
#print(cd-dob)
print((cd-dob).days//360)
