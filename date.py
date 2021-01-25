from datetime import date

today = date.today()
print("Today's date:", today)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)