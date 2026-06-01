from period import Period
from constants import Month


start_year = 2024
start_month = Month.JANUALY

period = Period(start_year, start_month, 23)

print(f"start: {period.start}")
print(f"end: {period.end}")