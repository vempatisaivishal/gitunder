#sum of subsequences must have even *odd must be odd
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    total=sum(l)
    lsum,rsum=0,0
    flag=True
    for i in range(len(l)):
        lsum+=l[i]
        rsum=total-lsum
        if((lsum*rsum)%2):
            print("YES")
            flag=False
            break
    if flag:
        print("NO")