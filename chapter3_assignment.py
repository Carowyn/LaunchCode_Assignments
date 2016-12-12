# TODO calculate the temperature, and report it back to the user

all_clicks = int(input("By how many clicks-to-the-right has the dial been turned?"))

if all_clicks > 50:
    clicks = (all_clicks % 50)
    temp = 40 + clicks
    print("The temperature is set to", temp, "degrees.")
else:
    temper = 40 + all_clicks
    print("The temperature is set to", temper, "degrees.")
