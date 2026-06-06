#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
#инкремента и декремента значения
class Counter:

    def __init__(self, value=0):
        self.value = value

    def increment(self, amount=1):
        self.value += amount

    def decrement(self, amount=1):
        self.value -= amount

    def get_value(self):
        return self.value

counter = Counter(10)
print(counter.get_value())
counter.increment(5)
print(counter.get_value())
counter.decrement(3)
print(counter.get_value())