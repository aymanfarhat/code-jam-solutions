import math

roots = {}

def checkPal(num):
	n = num
	rev = 0
	while num > 0:
		dig = num % 10
		rev = rev * 10 + dig
		num = num /10

	return n == rev

f = open("C-large-1.in")
lines = f.readlines()
f.close()

lines = map(lambda s:s.strip('\n'),lines)

T = lines[0]
cases = map(lambda l: l.split(" "),lines[1:])

res = []
count = 0

for i,case in enumerate(cases):
	a_range = [x for x in range(int(math.ceil(math.sqrt(int(case[0])))),int(math.sqrt(int(case[1])))+1)]
	count = 0
	
	for n in a_range:
		root = int(math.sqrt(n))
	
		if (root**2 == n) and checkPal(n) and checkPal(root):
			count += 1
	
	res.append("Case #{0}: {1}".format(i+1,count))
	print str(i+1)

f = open("result.out","w")
f.write("\n".join(map(lambda x: str(x),res)))
f.close()



