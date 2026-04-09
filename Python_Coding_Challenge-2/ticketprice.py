# Take day input
day = input("Enter day: ").lower()

# Determine ticket price based on day
if day == "saturday" or day == "sunday":
    print("Ticket Price: 200")   # Weekend price
else:
    print("Ticket Price: 100")   # Weekday price