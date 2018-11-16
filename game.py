def print_game(game):
	i = 1
	print("   ",1,"  ",2,"  ",3)
	for row in game:
		print(i,"[",row[0],"][", row[1],"][", row[2],"]")
		i+=1

def game_finished(game):
	# Vencedor linhas
	for row in game:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True
	
	# Vencedor colunas
	for i in range(len(game)):
		print(i)	

	return False


def main(game):
	while (game_finished(game) == False):
		print_game(game)

game = [[" "," "," "],[" "," "," "],[" "," "," "]]
main(game)
