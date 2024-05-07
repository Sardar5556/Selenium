from selenium import webdriver
import random
from datetime import datetime, timedelta

# Initialize the WebDriver
driver = webdriver.Chrome()

# Get today's date
today = datetime.now().date()

# Get the last day of the current month
last_day_of_month = (today.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

# Calculate the number of days remaining in the month
days_remaining = (last_day_of_month - today).days

# Generate a random integer representing the day of the month
random_day = today.day + random.randint(0, days_remaining)

print("Random day of the month:", random_day)

# Close the WebDriver
driver.quit()
