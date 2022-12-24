str=input("请输入字符串:")
key=input("请输入密钥:")
l=len(str)
m=len(key)
#加密过程
for i in range(l):
    index=i%m
    str=str[:i]+chr((ord(str[i])-ord('a')+ord(key[index])-ord('A'))%26+ord('A'))+str[i+1:]
print("加密密文为:")
print(str)
#解密过程
for i in range(l):
    index=i%m
    str=str[:i]+chr((ord(str[i])-ord('A')-( ord(key[index])-ord('A') ) )%26+ord('a'))+str[i+1:]
print("解密明文为:")
print(str)

