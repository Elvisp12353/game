#!/ust/bin/python3
__author__ ="ELvis Genao"
__copyright__ ="Copyright"
__credits__ ="Codigo elvis"
__license__ ="GPl"
__version__ ="1.0.1"
__maintainer__ ="Eduardo Ismael"
__email__ ="elvisp12353@gmail.com"
__status__ ="Developer"

"""
Este modulo se encarga de crear las fichas
"""
class pieces:
    def __init__(self,value = 0,desc = "none",win_to ="",lose_to=""):
        self.value = value
        self.desc = desc
        self.win_to = win_to
        self.lose_to = lose_to
class player:
    def __init__(self,choice="null",status ="nully",count=0):
        self.choice = choice
        self.status = status
        self.count = count

    def pick_piece(self,input):
        """
        Esta funcion hace que el usuario escoja una ficha
        """
        self.choice = pieces_list[input]



rock = pieces(1,"rock","scissors","paper")
paper = pieces(2,"paper","rock","scissors")
scissors = pieces(3,"scissors","paper","rock")

pieces_list = {
    1:rock.desc,
    2:paper.desc,
    3:scissors.desc,
}
