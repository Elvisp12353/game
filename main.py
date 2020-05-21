import objets 
selection = "seleccione \n 1 para piedra \n 2 para papel \n 3 para tijeras"




player1 =  objets.player()
print(selection)
player1.choice = objets.pieces_list[int(input())]


player2 =  objets.player()
print(selection)
player2.choice = objets.pieces_list[int(input())]   


