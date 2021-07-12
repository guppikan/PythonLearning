'''datatime module has been used to get current datetime'''

from datetime import date, datetime

# getting current date and time
current_datetime = datetime.now()

# getting time stamp of current date and time
timestamp = datetime.timestamp(current_datetime)

print("The current date and time :", current_datetime)
print("The time stamp :", timestamp)
