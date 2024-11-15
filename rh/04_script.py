#strings

# \ooo
# \xhhh
# \uxxxx
# \Uxxxxxxxx

url = "www.redhat.com"
result = url.startswith("www")
print((url, result))
result = url.endswith(".org")
print((url, result))
result = url.upper()
print((url, result))

# string_types

print("AbCdE".isalpha(),"AbCdE256".isalpha())
print("12533".isnumeric(),"2546a".isnumeric())
print("  \t\n".isspace(),"a b \t\n".isspace())
print("ABCDE".isupper(),"abcde".isupper())

#search

word = "is"
sentence = "the capital of Colombia is Bogota, and Bogota is cold"
print("Index",sentence.find(word))
print("Exist",word in sentence)
print("Times",sentence.count(word))

print("Justified right:",word.rjust(15),"|")
print(" :Justified left",word.ljust(15,"*"),"|")