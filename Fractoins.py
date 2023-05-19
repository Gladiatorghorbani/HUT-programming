str1 = input('Enter the first number:')
str2 = input('Enter the second number:')

numbers_1, numbers_2 = [],[]
result = []
#put numbers in the list
for i in range(0, len(str1)):
    numbers_1.append(int(str1[i]))

for i in range(0, len(str2)):
    numbers_2.append(int(str2[i]))

len1 = len(str1)
len2 = len(str2)

numbers_1.reverse()
numbers_2.reverse()

#more digits
def make_digits_equal(len1, len2):
    if len1 < len2:
        for i in range(0, len2 - len1):
            numbers_1.append(0)
    elif len1 > len2:
        for i in range(0, len1 - len2):
            numbers_2.append(0)
    else:
        pass
make_digits_equal(len1, len2)

print(numbers_1)
print(numbers_2)


carry = 0
i = 0
while True:
    result.append((numbers_1[i] + numbers_2[i] + carry) % 10)
    carry = (numbers_1[i] + numbers_2[i]) // 10

    #if len1 > len2:
    i += 1
    if i == len1:
        #if len(result) != len1:

        break
    #if len1 <= len2:

result.reverse()
#for i in range(0, len(result)):
#    print(result[i], end='')
for i in range(0,len(result)):
    print(result[i], end='')