
'''
set = conjunto

'''

# genera un set ordenado
set_01 = set('hola mundo')
print(set_01)

set_02 = set({1,9,5,6,8,2,4,7,6,3})
print(set_02)

set_03 = set([1,9,5,6,8,2,4,7,6,3])
print(set_03)

set_04 = set([ x for x in range(0,10)])
print(set_04)

'''
Argentina, Bolivia, Brasil, Chile, Colombia, Ecuador, Guyana, Paraguay, Perú, Surinam, Uruguay y Venezuela
'''
countries = {'col','ven','per','bol','ecu','bra','arg','uru','par','chi'}
set_merco = {'bol','bra','arg','uru','par'}
set_can = {'col','per','bol','ecu'}
unasur = set()

unasur.add('guy')
unasur.add('pan')
unasur.update({'col','ven','per','bol','ecu','bra','arg','uru','par','chi'})
#unasur.remove('pan')
unasur.discard('pan')
#unasur.clear()

print(unasur)

print('01 -----------------')
print('col' in unasur)
print('pan' not in unasur)

print('02 -----------------')
# inter
print(set_can.intersection(set_merco))
print(set_can & set_merco)

print('03 -----------------')
# union
print(set_can.union(set_merco))
print(set_can | set_merco)

print('04 -----------------')
# dif
print(set_can.difference(set_merco))
print(set_can - set_merco)

print(set_can.difference_update(set_merco))
print(set_merco.difference_update(set_can))

print('05 -----------------')
# sim
print(set_can.symmetric_difference(set_merco))
print(set_can ^ set_merco)

print('06 -----------------')
# sim
print(set_merco.issubset(countries))
print(set_merco <= countries)

print('07 -----------------')
#
print(set_merco.isdisjoint(countries))
print(countries.isdisjoint(set_merco))
print('-------------------')
