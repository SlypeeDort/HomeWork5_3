class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors >= new_floor > 0:
            for i in range(new_floor):
                print(f'Этаж   {i + 1}')
        else:
            print('Такого этажа не существует"')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name

    def __iadd__(self, other):
        self.number_of_floors += other
        return self

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(f'Название: {str(h1)}, кол-во этажей: {len(h1)}')
print(f'Название: {str(h2)}, кол-во этажей: {len(h2)}')
print(h1 == h2)
h1.number_of_floors = len(h1).__add__(10)
print(f'Название: {str(h1)}, кол-во этажей: {len(h1)}')
print(h1 == h2)
h1.number_of_floors = len(h1.__iadd__(10))
print(f'Название: {str(h1)}, кол-во этажей: {len(h1)}')
print(h1 == h2)
h2.number_of_floors = len(h2).__radd__(10)
print(f'Название: {str(h2)}, кол-во этажей: {len(h2)}')
print(h1 == h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)