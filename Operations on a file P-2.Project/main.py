Out = open('upd.txt','w')

inputfile = open('c:/Users/Admin/Desktop/Python L1/Operations on a file P-2.Project/Hi.txt','r')
lines = set()

print("Duplicating Lines")

for line in inputfile :
    if line not in lines :
        Out.write(line)

        lines.add(line)
Out.close()
inputfile.close()











