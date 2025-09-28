# Program For DATE
from datetime import date
Date = date.today()
print("Today's Date is",Date)

# Program For TIME
import datetime
time_now = datetime.datetime.now()
Time = time_now.strftime("%H:%M:%S")
print("The curren Time is",Time)
