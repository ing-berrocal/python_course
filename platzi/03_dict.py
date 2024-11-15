a = dict({'key':1})
b = {'key':1}

b.update({"name":'Junior python developer',"age":30})

print(type(a))
print(type(b))

print(len(b))

print(b.get("name"))
print(b.get(1))

c = [ { i : i * 10 for i in range(100) }]

print(c)

import random

countries = {'col','ven','per','bol','ecu','bra','arg','uru','par','chi'}

d = {}
for country in countries:
    d[country] = random.randint(0,100)
print(d)

countries = ['col','ven','per','bol','ecu','bra','arg','uru','par','chi']
data = [ random.randint(100,1000) for x in range(len(countries)) ]

print("03 -----")

e = {}
for m,n in zip(countries, data) :
    e[m] = n
print(e)


f = { m : n for (m,n) in zip(countries, data) }
print(f)
    
