# Get input from the user
month = input("Enter the month (first three letters): ").lower()
day = int(input("Enter the day: "))

# Determine the season based on the input date
if (month == 'mar' and day >= 20) or (month == 'jun' and day < 21):
    season = 'Spring'
elif (month == 'jun' and day >= 21) or (month == 'sep' and day < 22):
    season = 'Summer'
elif (month == 'sep' and day >= 22) or (month == 'dec' and day < 21):
    season = 'Fall'
else:
    season = 'Winter'

# Display the season
print(f"The season for {month.capitalize()} {day} is {season}.")
