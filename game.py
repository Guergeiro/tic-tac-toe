def print_game(game):
	i = 1
	print("X\Y",1,"  ",2,"  ",3)
	for row in game:
		print(i,"[",row[0],"][", row[1],"][", row[2],"]")
		i+=1

def checker(thing):
	if thing.count(thing[0]) == len(thing) and thing[0] != " ":
		return True
	return False

def game_finished(game):
	# Vencedor linhas
	for row in game:
		if checker(row):
			print("ROW")
			return True
	
	# Vencedor colunas
	for i in range(len(game)):
		columns = []
		for row in game:
			columns.append(row[i])
		if checker(columns):
			print("COL")
			return True

	# Vencedor diagonal
	# Diagonal Esq->Dir
	diags = []
	for i in range(len(game)):
		diags.append(game[i][i])
	if checker(diags):
		print("DIAG1")
		return True
	#Diagonal Dir->Esq
	diags = []
	for i in range(len(game)):
		diags.append(game[i][len(game)-1-i])
	if checker(diags):
		print("DIAG2")
		return True	
	return False

def play(game, optionX=0, optionY=0, player=" "):
	options = [1,2,3]
	# Not in range of list
	if ((optionX not in options) or (optionY not in options)):
		return True
	# Spot already taken
	elif game[optionX-1][optionY-1] != " ":
		return True

	game[optionX-1][optionY-1] = player
	return False

def main(game):
	players = ["X","O"]
	i = 0
	while (game_finished(game) == False):
		print_game(game)
		print("Player: ", players[i])
		optionX = input("X: ")
		optionY = input("Y: ")
		result = play(game, int(optionX), int(optionY), players[i])
		if result==True:
			print("Play again")
			continue
		if i == 0:
			i = 1
		else:
			i = 0

game = [[" "," "," "],[" "," "," "],[" "," "," "]]
main(game)
