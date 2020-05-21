class pieces:
    def __init__(self,value = 0,desc = "none",win_to ="",lose_to=""):
        self.value = value
        self.desc = desc
        self.win_to = win_to
        self.lose_to = lose_to
class player:
    def __init__(self,choice="null",status ="nully"):
        self.choice = choice
        self.status = status



rock = pieces(1,"piedra","scissors","paper")
paper = pieces(2,"papel","rock","scissors")
scissors = pieces(3,"tijeras","paper","rock")

pieces_list = {
    1:rock,
    2:paper,
    3:scissors,
}