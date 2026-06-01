from period import Period
from constants import Month


start_year = 2024
start_month = Month.JANUALY

end_year = 2025
end_month = Month.DECEMBER

period = Period(start_year, start_month, end_year, end_month)

print(f"start: {period.start}")
print(f"end: {period.end}")