"""
This module just contains this class
"""
import config

class NewYearController:
    """
    This class simply changes the colour of Option 0 on the screen
    depending on whether it's enabled or not.
    """
    def __init__(self, year_finished):
        self.year_finished = True if year_finished == 'y' else False
        self.color = config.COLOR_STRONG_WHITE if year_finished == 'y' else config.COLOR_NORMAL

    def year_finished(self):
        return self.year_finished

    def color(self):
        return self.color
