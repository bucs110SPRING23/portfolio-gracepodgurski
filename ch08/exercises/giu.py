# Classes of Super Mario Bros

class Background:
    def __init__(self):
        self.worlds = 8
        self.stages = 4
        self.clouds = "white"
        self.bkgd_color = "blue"

class Boxes:
    def __init__(self):
        self.icon = "square", "?"
        self.contains_coin = True

class Score:
    def __init__(self):
        self.start = 0
        self.coin = self + 5
