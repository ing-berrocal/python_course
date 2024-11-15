def find_volume(length=1, width=2, depth=-1):
    return length * width * depth

result = find_volume()

print(result)

result1 = find_volume(width=20)

print(result1)

result2 = find_volume(20)

print(result2)

#Retorno de multiple parametros, tupla
def return_tuple(a,b):
    return a * 2, b ** 2

result = return_tuple(2,3)
print(result)
print(result[0])

result_a, result_b = return_tuple(4,16)

print(result_a)
print(result_b)