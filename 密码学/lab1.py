str=input("输入一个字符串")
key=input("选取密钥:")
l=len(str)
s1,s2=str,str
for i in range(l):
    if str[i]>='a'and str[i]<='z':
        s1=s1[:i]+chr((ord(str[i])-ord('a')+eval(key))%26+ord('A'))+s1[i+1:]
print("密文为:")
print(s1)
for i in range(l):
        s2=s2[:i]+chr((ord(s1[i])-ord('A')-eval(key))%26+ord('a'))+s2[i+1:]
print("明文为:")
print(s2)
