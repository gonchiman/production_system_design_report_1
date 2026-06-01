class Period:
    def __init__(self, start_year: int, start_month: str, end_year: int, end_month: str):
        start = str()
        end = str()
        self.set_start(start_year, start_month)
        self.set_end(end_year, end_month)

    def set_start(self, start_year, start_month):
        self.start = f"{str(start_year)} {start_month}"

    def set_end(self, end_year, end_month):
        self.end = f"{str(end_year)} {end_month}"