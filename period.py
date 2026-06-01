from constants import MONTH_NUMS


class Period:
    def __init__(self, start_year: int, start_month: str, duration: int):
        start = str()
        end = str()
        self.set_start(start_year, start_month)
        self.set_end(start_year, start_month, duration)

    def set_start(self, start_year, start_month):
        self.start = f"{start_month} {str(start_year)}"

    def set_end(self, start_year, start_month, duration):
        end_month_num = MONTH_NUMS.get(start_month, 1) + duration - 1
        end_year = start_year + end_month_num // 12
        end_month = list(MONTH_NUMS.keys())[list(MONTH_NUMS.values()).index(end_month_num % 12 + 1)]

        self.end = f"{end_month} {str(end_year)}"