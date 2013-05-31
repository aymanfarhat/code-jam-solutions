# Parses each string patterns to list of strings and lists(options)
def parse_patterns(patterns):
    lines = []

    def getclosing(i,pattern):
        for x in xrange(i,len(pattern)):
            if pattern[x] == ")":
                return x
        return -1

    for pattern in patterns:
        line = []
        i = 0
        
        while i < len(pattern): 
            if pattern[i] == "(":
                j = getclosing(i,pattern)
                
                if j > i and j-i > 2:
                    line.append(list(pattern[i+1:j]))
                    i = j

            elif pattern[i] != ")":
                line.append(pattern[i])
            i += 1

        lines.append(line)

    return lines

# Check if a string matches a pattern represented as a list
def checkmatch(word, pattern):
    for i,el in enumerate(word):
        return !(type(pattern[i]) == str and el != pattern[i]) or (type(pattern[i])==list and el not in pattern[i]):
    return True

f = open('A-large-practice.in')
lines = f.readlines()
f.close()

L, D, N = map(int,lines[0].rstrip('\n').split(' '))

# Get list of all alien words
words = [w.rstrip('\n') for w in lines[1:D+1]]

# Get list of patters and parse them
p_patterns = parse_patterns([w.rstrip('\n') for w in lines[(D+1):(D+N+1)]])

# Keep track of number of matches for each pattern here
matches = [0]*len(p_patterns)

# Check every word for matching with any pattern
for word in words:
    for i, pattern in enumerate(p_patterns):
        if checkmatch(word,pattern):
            matches[i] += 1

# Printe results
for i in xrange(0,len(matches)):
    print "Case #{0}: {1}".format(i+1,matches[i])