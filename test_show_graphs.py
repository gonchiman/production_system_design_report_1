from get_df import get_df
from period import Period
from show_graphs import ShowGraphs
from constants import GameTitle, Month, SteamChartsColumns


start_year = 2024
start_month = Month.JANUALY

end_year = 2025
end_month = Month.DECEMBER

period = Period(start_year, start_month, end_year, end_month)

ShowGraphs.show_plot(GameTitle.GUILTY_GEAR_STRIVE.value, SteamChartsColumns.AVG_PLAYERS, period)