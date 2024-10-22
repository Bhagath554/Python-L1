def onf1(n):
  iteration = 0
  for i in range (0,n):
    for j in range (0,n):
      print("Hello",end="")
      iteration+=1
    print("")

  print("\n When n is ",n,"Iterations = ",iteration,"\n")

onf1(4)
onf1(5)
onf1(3)

print("\n With every 'n' the time taken equals n^2")
print("O(n^2)")