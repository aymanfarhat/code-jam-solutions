# Open input file
f = open('A-large-practice.in')
lines = f.readlines()
f.close()

#String to list of ints conversion 
def str_int_list(s):
    return map(lambda s: int(s), s.split())

# Iterate over the input converting to vectors and computing
T = int(lines[0])
case = 1
i = 1

results = []

while(case <= T):
    v1 = str_int_list(lines[i+1])
    v2 = str_int_list(lines[i+2])

    # Sort v1 in decreasing order and v2 to increasing then multiply
    v1.sort()
    v2.sort(reverse = True)

    product = [a * b for a,b in zip(v1,v2)]
    results.append("Case #{0}: {1}".format(case,str(sum(product))))

    i = i + 3
    case += 1

# Output results to file
f = open("result.out", "w")
f.write("\n".join(results))
f.close()
