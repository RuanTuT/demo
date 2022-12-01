n=eval(input("输入一个数："))
if n==1 or n%2==0 and n>2:
    print("不是素数")
else:
    ct=2
    while ct<n:
        if n%ct==0:
           break
        else:
            ct=ct+1
    if  ct>=n:
        print("是素数")
    else:
        print("不是素数")

