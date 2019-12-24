class A:
    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age

    def average_height(self):
        total = sum(self.height)
        averages = total / len(self.height)
        print(float(averages))

    def average_weight(self):
        total = sum(self.weight)
        averages = total / len(self.weight)
        print(float(averages))

    def average_age(self):
        total = sum(self.age)
        averages = total / len(self.age)
        print(float(averages))


class B(A):
    def average_height(self):
        total = sum(self.height)
        averages = total / len(self.height)
        print(float(averages))

    def average_weight(self):
        total = sum(self.weight)
        averages = total / len(self.weight)
        print(float(averages))

    def average_age(self):
        total = sum(self.age)
        averages = total / len(self.age)
        print(float(averages))
if A.average_height > B.average_height:
    print("A")
if A.average_height < B.average_height:
    print("B")
if A.average_height == B.average_height:
   if A.average_weight< B.average_weight:
for x in range(2):
    x = int(input())
    for i in range(3):
        my_input = [int(x) for x in input().split()]
x1 = A(my_input)
x1.average_height()
x1.average_weight()
x1.average_age()
x2 = B(my_input)