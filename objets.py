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



rock = pieces(1,"rock","scissors","paper")
paper = pieces(2,"paper","rock","scissors")
scissors = pieces(3,"scissors","paper","rock")

pieces_list = {
    1:rock.desc,
    2:paper.desc,
    3:scissors.desc,
}
print(pieces_list[1])