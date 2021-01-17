class Add:
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    def __str__(self):
        return self.num1 + self.num1


obj = Add(3, 4)
print(obj)