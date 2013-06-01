import string

mapping = {}

inp = ("ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv")

output = ("our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up")

alfai = lambda x: string.lowercase.index(x)

for i, o in zip(inp,output):
    pairs = (i,o)
    
    for c in xrange(len(pairs[1])):
        if pairs[1][c].isalnum(): 
            mapping[pairs[0][c]] = pairs[1][c]

mapping["q"]="z"

f = open('A-small-practice.in')
lines = f.readlines()
f.close()

del lines[0]

f_out = open('result.out','w')

for i in xrange(len(lines)):
    linestr = ""
    for c in lines[i].rstrip('\n'):
        if c != " ":
            if c not in mapping:
                linestr += "q"
            else:
                linestr += mapping[c]
        else:
            linestr += " "
    
    f_out.write("Case #{0}: {1} \n".format(i+1,linestr))

f_out.close()
