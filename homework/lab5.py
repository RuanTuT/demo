def Extended_Eulid(a,n):
    x1 = 1
    x2 = 0
    x3 = n
    y1 = 0
    y2 = 1
    y3 = a
    while y3>1:
        q=x3//y3
        t1=x1-q*y1
        t2 = x2 - q*y2
        t3 = x3 - q*y3
        x1 = y1
        x2 = y2
        x3 = y3
        y1 = t1
        y2 = t2
        y3 = t3
    if y3==0:
        return -1#这时x3=gcd(a , n) , a-1不存在
    else:
        return  y2#这时y3=gcd(a , n)=1, y2=a-1(mod n)
a=eval(input("请输入a："))
n=eval(input("请输入n："))
print(Extended_Eulid(a,n))