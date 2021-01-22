import itertools as its
words="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
dic=open('pwdLists4.txt','w')

keys=its.product(words,repeat=4)
for key in keys:
    dic.write("".join(key)+"\n")

dic.close()