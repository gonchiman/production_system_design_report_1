import requests


class GameTitle:
    STREET_FIGHTER_6 = "Street Fighter 6"
    TEKKEN_8 = "TEKKEN 8"
    GUILTY_GEAR_STRIVE = "GUILTY GEAR -STRIVE-"
    GRANBLUE_FANTASY_VERSUS_RISING = "Granblue Fantasy Versus: Rising"
    THE_KING_OF_FIGHTERS_XV = "THE KING OF FIGHTERS XV"

GAMES = {
    "Street Fighter 6": 1364780,
    "TEKKEN 8": 1778820,
    "GUILTY GEAR -STRIVE-": 1384160,
    "Granblue Fantasy Versus: Rising": 2157560,
    "THE KING OF FIGHTERS XV": 1498570,
}

game_title = GameTitle.STREET_FIGHTER_6

appid = GAMES[game_title]

url = f"https://steamcharts.com/app/{appid}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=10)

print(response.status_code)
print("Avg. Players" in response.text)
print("Peak Players" in response.text)
print("Month" in response.text)