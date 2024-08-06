#!/usr/bin/env python3

'this is a literal string'
"this is a literal string"

#Escape

print("This is 'a' literal string")
print("This is \"a\" literal string")

largestring = 'this is a long string\n\
    that span multple lines.'

print(largestring)

bigger = """
This is an even
bigger string that
spans three lines.
"""

print(bigger)


mystr = "my string"
print(mystr[0]) # 'm'
print(mystr[-2]) # 'n'


for c in mystr:
    print(c)

def my_func_to_upper(txt):
    return txt.upper()

result = [ my_func_to_upper(c) for c in mystr];

print(result)

ejem_h = "hola"

print(ejem_h.ljust(20,'+'))
print(ejem_h.rjust(20,'+'))
print(ejem_h.center(20,'+'))


ejem_s = "        hola            "
print(ejem_s.strip())

revwords = mystr.split()
revwords.reverse()
revwords = ' '.join(revwords)

print(revwords)

def containsAny(seq, aset):
    """ Check wheter sequence seq contains ANY of then items in aset. """
    for c in seq:
        if c in aset: return True
    return False

ejem_1 = "Hola este es un texto el cual se buscara una sequencia"
aset_1 = "s"
aset_2 = "z"

print(containsAny(ejem_1,aset_1))
print(containsAny(ejem_1,aset_2))
