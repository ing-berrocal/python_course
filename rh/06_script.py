#

counter=0
total = 10

while counter < total:
    counter += 1
    print("Running counter =",counter)

#break
# 

cnt = 0
total = 0

while cnt <= 100:
    cnt += 1
    if cnt % 4 == 0:
        continue
    if cnt * cnt > 400:
        break
    total += cnt

print("Total is:", total," Count is:",cnt)

# for

word = "Hello"

for each_word in word:
    print(each_word,end="\t")

for i in range(0,10):
    print(i)

#
print("*"*50)
text = """ Each word is separated
by whitespace
"""
data = text.split()
for value in data:
    print(value)

#
print("*"*50)