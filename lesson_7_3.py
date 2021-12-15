# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В
# его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    __count_cell: int

    def __init__(self, count_cell: int):
        self.__count_cell = count_cell

    def __add__(self, other):  # сложение
        value = self.count + other.count
        return Cell(value)

    def __sub__(self, other):  # вычитание
        value = self.count - other.count
        return Cell(value)

    def __mul__(self, other):  # умножение
        value = self.count * other.count
        return Cell(value)

    def __truediv__(self, other):  # деление
        value = round(self.count / self.count)
        return Cell(value)

    def __str__(self):
        return str(self.__count_cell)

    @property
    def count(self):
        return self.__count_cell

    @staticmethod
    def make_order(cell_object: 'Cell', count_per_row: int):
        items = '*' * cell_object.count
        block = [
            items[idx:idx + count_per_row]
            for idx in range(0, len(items), count_per_row)
        ]
        return '\n'.join(block)


a = Cell(12)
b = Cell(7)
c = Cell(17)

print(f"Сложение:  {a} + {b} = {a + b}")
print(f"Вычитание: {a} - {b} = {a - b}")
print(f"Умножение: {a} * {b} = {a * b}")
print(f"Деление:   {a} / {b} = {a / b}")
print(f"Вывод метода make_order({c}, 5)")
print(Cell.make_order(c, 5))