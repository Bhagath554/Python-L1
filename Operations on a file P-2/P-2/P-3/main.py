Output = open('Upd.txt','w')

inputfile = open('c:/Users/Admin/Desktop/Python L1/Operations on a file P-2/P-2/P-3/Hello.txt','r')
lines = set()

print("Duplicating Lines")

for line in inputfile :
    if line not in lines :
        Output.write(line)

        lines.add(line)
Output.close()
inputfile.close()