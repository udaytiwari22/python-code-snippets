n=int(input())
li=[int(x) for x in input().split()]
ele=int(input())
flag = False
for i in range(len(li)):
    if li[i]==ele:
        print(i)
        flag=True
        break
if flag== False:
    print(-1)        
