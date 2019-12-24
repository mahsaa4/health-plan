class ClassRoom:
    def __init__(self, height, weight, age, count):
        self.height = height
        self.weight = weight
        self.age = age
        self.count = count

    def average_height(self):
        return sum(self.height) / self.count

    def average_weight(self):
        return sum(self.weight) / self.count

    def average_age(self):
        return sum(self.age) / self.count


if __name__ == '__main__':
    classrooms = []
    for student in range(2):
        x = int(input())
        ages = list(map(int, input().split()))
        height = list(map(int, input().split()))
        weight = list(map(int, input().split()))
        class_room = ClassRoom(age=ages, height=height, weight=weight, count=x)
        classrooms.append(class_room)

    class_a = classrooms[0]
    class_b = classrooms[1]

    print(class_a.average_age())
    print(class_a.average_height())
    print(class_a.average_weight())
    print(class_b.average_age())
    print(class_b.average_height())
    print(class_b.average_weight())

    a_average_heights = class_a.average_height()
    b_average_heights = class_b.average_height()
    a_average_weight = class_a.average_weight()
    b_average_weight = class_b.average_weight()

    if a_average_heights > b_average_heights:
        print("A")
    elif a_average_heights < b_average_heights:
        print("B")
    else:
        if a_average_weight < b_average_weight:
            print("A")
        elif a_average_weight > b_average_weight:
            print("B")
        else:
            print("Same")
