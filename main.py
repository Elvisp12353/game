import objets 
selection = "seleccione \n 1 para piedra \n 2 para papel \n 3 para tijeras"

player1 =  objets.player()
print(selection)
player1.pick_piece(int(input()))


player2 =  objets.player()
print(selection)
player2.pick_piece(int(input()))
   

if player1.choice == player2.choice:
    player1.status = "draw"
    player2.status = "draw"
    print("This game is draw")


