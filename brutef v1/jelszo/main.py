import string
import random

# letters

letter = (string.ascii_lowercase+"0"+"1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9")
letterlis = list(letter)
print(letterlis)

jelszo = input("mi a jelszavad?")

tipp = []
megoldott=0

x=0
chars=(len(letterlis))
chars-=1

while megoldott == 0:
    print(letterlis[x])
    if (letterlis[x])==jelszo:
        megoldas=(letterlis[x])
        megoldott=1
    elif x==chars:
        break
    else:
        x+=1

x=0
y=0

while megoldott==0:
    megoldas=(letterlis[x]+letterlis[y])
    print (megoldas)
    if x==chars:
        break
    elif y==chars:
        x+=1
        y=0
    elif megoldas==jelszo:
        megoldott = 1
    else:
        y+=1

x=0
y=0
z=0

while megoldott==0:
    megoldas=(letterlis[x]+letterlis[y]+letterlis[z])
    print(megoldas)
    if x==chars:
        break
    elif megoldas==jelszo:
        megoldott=1
    elif z==chars:
        y+=1
        z=0
    elif y==chars:
        x+=1
        y=0
    else:
        z+=1

x=0
y=0
z=0
u=0

while megoldott==0:
    megoldas=(letterlis[x]+letterlis[y]+letterlis[z]+letterlis[u])
    if x==chars:
        break
    elif megoldas==jelszo:
        megoldott=1
    elif u==chars:
        z+=1
        u=0
    elif z==chars:
        y+=1
        z=0
    elif y==chars:
        x+=1
        y=0
    else:
        u+=1

x=0
y=0
z=0
u=0
v=0

while megoldott==0:
    megoldas=(letterlis[x]+letterlis[y]+letterlis[z]+letterlis[u]+letterlis[v])
    if x==chars:
        break
    elif megoldas==jelszo:
        megoldott=1
    elif v==chars:
        v=0
        u+=1
    elif u==chars:
        z+=1
        u=0
    elif z==chars:
        y+=1
        z=0
    elif y==chars:
        x+=1
        y=0
    else:
        v+=1

x=0
y=0
z=0
u=0
v=0
t=0

while megoldott==0:
    megoldas=(letterlis[x]+letterlis[y]+letterlis[z]+letterlis[u]+letterlis[v])
    if x==chars:
        break
    elif megoldas==jelszo:
        megoldott=1
    elif t==chars:
        v+=1
        t=0
    elif v==chars:
        v=0
        u+=1
    elif u==chars:
        z+=1
        u=0
    elif z==chars:
        y+=1
        z=0
    elif y==chars:
        x+=1
        y=0
    else:
        t+=1

print (megoldas)