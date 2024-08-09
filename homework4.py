class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # def go_to(self, new_floor):
    #     self.new_floor = new_floor
    #     if new_floor >= 1 and new_floor < self.number_of_floors:
    #         for i in range(1, new_floor + 1):
    #             print(i, end=" ")
    #     else:
    #         print("Такого этажа не существует")
    #
    # def __len__(self):
    #     return self.number_of_floors
    #
    # def __str__(self):
    #     return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    # print("")
    #
    # def __eq__(self, other):
    #     isinstance(other, int)
    #     isinstance(other, House)
    #     return self.number_of_floors == other.number_of_floors
    #
    # def __lt__(self, other):
    #     isinstance(other, int)
    #     isinstance(other, House)
    #     return self.number_of_floors < other.number_of_floors
    #
    # def __le__(self, other):
    #     isinstance(other, int)
    #     isinstance(other, House)
    #     return self.number_of_floors <= other.number_of_floors
    #
    # def __gt__(self, other):
    #     isinstance(other, int)
    #     isinstance(other, House)
    #     return self.number_of_floors > other.number_of_floors
    #
    # def __ge__(self, other):
    #     isinstance(other, int)
    #     isinstance(other, House)
    #     return self.number_of_floors >= other.number_of_floors
    #
    # def __ne__(self, other):
    #     isinstance(other, int)
    #     isinstance(other, House)
    #     return self.number_of_floors != other.number_of_floors
    #
    # def __add__(self, value):
    #     isinstance(value, int)
    #     return self.number_of_floors + value
    #
    # def __radd__(self, value):
    #     isinstance(value, int)
    #     return self.number_of_floors + value
    #
    # def __iadd__(self, value):
    #     isinstance(value, int)
    #     return self.number_of_floors + value

    def __del__(self):
        if self.name in House.houses_history:
            print(f'{self.name} снесён, но он останется в истории')
            return House.houses_history.remove(self.name)


h1 = House("ЖК Онегин", 20)
print(House.houses_history)
h2 = House("ЖК Квартет", 10)
print(House.houses_history)
h3 = House("ЖК Салют", 18)
print(House.houses_history)
del h2
print(House.houses_history)
del h1
print(House.houses_history)
