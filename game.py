def print_game(game):
	i = 1
	print("X\Y",1,"  ",2,"  ",3)
	for row in game:
		print(i,"[",row[0],"][", row[1],"][", row[2],"]")
		i+=1

def game_finished(game):
	# Vencedor linhas
	for row in game:
		if row.count(row[0]) == len(row) and row[0] != " ":
			print("ROW")
			return True
	
	# Vencedor colunas
	for i in range(len(game)):
		columns = []
		for row in game:
			columns.append(row[i])
		if columns.count(columns[0]) == len(columns) and columns[0] != " ":
			print("COL")
			return True

	# Vencedor diagonal
	# Diagonal Esq->Dir
	diags = []
	for i in range(len(game)):
		diags.append(game[i][i])
	if diags.count(diags[0]) == len(diags) and diags[0] != " ":
		print("DIAG1")
		return True
	#Diagonal Dir->Esq
	diags = []
	for i in range(len(game)):
		diags.append(game[i][len(game)-1-i])
	if diags.count(diags[0]) == len(diags) and diags[0] != " ":
		print("DIAG2")
		return True	
	return False

def play(game, optionX, optionY, player):
	if (optionX, optionY) < 1 or (optionX,optionY) > len(game) 
		return True

	game[optionX][optionY] = player
	return False

def main(game):
	players = ["X","O"]
	while (game_finished(game) == False):
		print_game(game)
		optionX
		optionY
		while(play(game,optionX , optionY, player)):
			optionX = input("X: ")
			optionY = input("Y: ")

game = [["X"," ","X"],[" "," "," "],["X"," "," "]]
main(game)
