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
        self.location = (x,y)
        self.size = (height,width)
        self.contains_coin = True
        self.is_mystery = bool
        # this can be used for the ground as well 
        # can inherit block into a power up catagory 

class Score:
    def __init__(self):
        self.start = 0
        self.coin = self + 5 #this should not be in a class bc it is for the controller 

class Text:
    def __init__(self):
        self.font = "font"
        self.size = 20
        self.pos = (x,y)
        self.color = "white"
        self.msg = "--"

