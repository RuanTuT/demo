str=input('请输入需要解密的序列')
str1=['A','B','C' ,'D' ,'E', 'F', 'G' ,'H' ,'I' ,'J', 'K' ,'L' ,'M' ,'N' ,'O', 'P' ,'Q' ,'R' ,'S', 'T', 'U' ,'V' ,'W' ,'X' ,'Y' ,'Z'];
str2=['d' ,'l', 'r', 'y' ,'v' ,'o' ,'h', 'e', 'z', 'x' ,'w' ,'p', 't', 'b' ,'g' ,'f' ,'j' ,'q' ,'n', 'm', 'u', 's', 'k', 'a' ,'c' ,'i' ];
s1,s2=str,str
l=len(str)
length=len(str2)
for i in range(l):
    if str[i] >= 'A' and str[i] < 'a':
        x=ord(str[i])-ord('A')
        s1=s1[:i]+str2[x]+s1[i+1:]
    if str[i]>='a'and str[i]<='z':
        for j in range(length):
            if str2[j]==str[i]:
                s1=s1[:i]+str1[j]+s1[i+1:]
print("明文序列为:")
print(s1)
for i in range(l):
    if str[i] >= 'A' and str[i] < 'a':
        x=ord(str[i])-ord('A')
        s1=s1[:i]+str2[x]+s1[i+1:]
    if str[i]>='a'and str[i]<='z':
        for j in range(length):
            if str2[j]==str[i]:
                s1=s1[:i]+str1[j]+s1[i+1:]

