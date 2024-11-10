a = 500
for n in range(1,a+1):
    c=0
    rev = 0
    num = n

    for p in range(1,num+1):
        if num%p==0:
            c+=1

    if c==2:
        while num>0:
            rev = rev*10+(num%10)
            num//=10

        if rev == n:
            print(n)