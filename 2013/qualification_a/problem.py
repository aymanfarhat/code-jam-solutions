def checkHorizontal(player,rows):
	for row in rows:
		if row.count(player) == 4 or (row.count(player) == 3 and row.count("T") == 1):
			return True
	return False

def checkVertical(player,rows):
	cols = len(rows)-1
	for i in xrange(cols):
		line = rows[0][i]+rows[1][i]+rows[2][i]+rows[3][i]
		if line.count(player) == 4 or (line.count(player) == 3 and line.count("T") == 1):
			return True
	return False

def checkDiag1(player,rows):
	line = rows[0][0]+rows[1][1]+rows[2][2]+rows[3][3]

	if line.count(player) == 4 or(line.count(player) == 3 and line.count("T") == 1):
		return True
	return False

def checkDiag2(player,rows):
	line = rows[0][3]+rows[1][2]+rows[2][1]+rows[3][0]
	if line.count(player) == 4 or (line.count(player) == 3 and line.count("T") == 1):
		return True
	return False

def isDone(rows):
	for row in rows:
		if "." in row:
			return False
	return True

def getWinner(aset):
	if checkHorizontal("X",aset) or checkVertical("X",aset) or checkDiag1("X",aset) or checkDiag2("X",aset):
		return "X"
	elif checkHorizontal("O",aset) or checkVertical("O",aset) or checkDiag1("O",aset) or checkDiag2("O",aset):
		return "O"
	else:
		return "none"

f = open("A-large.in")
lines = f.readlines()
f.close()

lines = map(lambda s: s.strip('\n'),lines)
T = lines[0]
lines = lines[1:]


sets = [lines[x:x+5] for x in xrange(0,len(lines),5)]

results = []

for i,aset in enumerate(sets):
	result = getWinner(aset)
	out = ""
		
	if result != "none":
		out = result+" won"
	elif (not isDone(aset)):
		out = "Game has not completed"
	else:
		out = "Draw"
	
	results.append("Case #{0}: {1}".format(i+1,out))

#print results
f = open("result.out",'w')
f.write("\n".join(map(lambda x: str(x),results)))
f.close()
