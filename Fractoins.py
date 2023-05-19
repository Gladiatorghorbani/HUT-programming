#add two fractions
#inout an string like this example
#str1 = '2/2 2/2'
str1 = input("Enter the fractions as string:")
index = []
for i in range(0, len(str1)):
    if str1[i] == '/' or str1[i] == ' ':
        index.append(i)
print(str1)
first_numerator = int(str1[: index[0]])
first_denominator = int(str1[index[0]+1 : index[1]])

second_numerator = int(str1[index[1]+1 : index[2]])
second_denominator = int(str1[index[2] + 1 :])

class Add():
    def __init__ (self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        denominator_result = self.denominator * other.denominator
        numerator_result= self.numerator * other.denominator + self.denominator * other.numerator
        return Add(numerator_result, denominator_result)

    def __repr__(self):
        return (f'{self.numerator}/{self.denominator}')



n1 = Add(first_numerator, first_denominator)
n2 = Add(second_numerator, second_denominator)
print(n1 + n2)
