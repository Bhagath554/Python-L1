def fun1(n):
    if(n>0):
        return
        for i in range(0,n+1):
            print("Codingal")
        myfun1(n/2)
        myfun1(n/3)


def myfun2(n):
    if(n<=0):
        return
    print("Coding")
    myfun(n-1)