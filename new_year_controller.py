import config

class NewYearController:
    def __init__(self, year_finished):
        self.year_finished = True if year_finished == 'y' else False
        self.color = config.COLOR_STRONG_WHITE if year_finished == 'y' else config.COLOR_NORMAL