with open('c:/Users/Admin/Desktop/Python L1/Operations on a file P-2/P-2/P-3/P-4/Codingal.txt') as fp:
    data1 = fp.read()

with open('c:/Users/Admin/Desktop/Python L1/Operations on a file P-2/P-2/P-3/P-4/Code.txt') as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging Two Files")
with open('c:/Users/Admin/Desktop/Python L1/Operations on a file P-2/P-2/P-3/P-4/Mergedfile.txt','w') as fp:
     fp.write(data1)
fp.close()
with open('c:/Users/Admin/Desktop/Python L1/Operations on a file P-2/P-2/P-3/P-4/Mergedfile.txt','r') as fp:
    fp.read()
    print(fp.read())


