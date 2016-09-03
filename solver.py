WIN = "win"
LOSE = "lose"
UNDECIDED = "undecided"

def initial_position():
	return 4

def primitive(pos):
	if not pos:
		return LOSE #lost the game
	elif pos == 1 or pos == 2:
		return WIN
	return UNDECIDED #game is still undecided
	

def gen_moves(pos): #generates the possible actions (-1 and/or -2)
	moves = []
	if pos - 1 >= 0:
		moves += [-1]
	if pos - 2 >= 0:
		moves += [-2]
	return moves

def do_move(pos, move):
	pos = pos + move
	return pos

def four_to_zero_solver(initial_position, primitive, do_move, gen_moves):
	pos = initial_position()
	results = {}
	results[pos] = null
	def solve(dicti, pos):
		moves = gen_moves(pos)
		for move in moves:
			next_step = do_move(pos, move)
			if next_step not in dicti:
				dicti[next_step] = solve(results, next_step)
		return primitive(pos)
	solve(results, pos)
	return results[pos]