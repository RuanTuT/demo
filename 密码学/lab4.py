
def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)
x=eval(input("输入第一个数:"))
y=eval(input("输入第二个数:"))
print(gcd(x,y))