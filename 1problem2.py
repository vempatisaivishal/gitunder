#we need to have min number of 1's in binary but max(bi,b(i+1))=1 so every alternate should be 1
t=int(input())
for i in range(t):
    n=int(input())
    print(n//2)#this used for ground division