"""
Продемонстрируйте полиморфизм
Используйте композицию
Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу,
такие как сохранение информации о зоопарке в файл и
возможность её загрузки, чтобы у вашего зоопарка было
"постоянное состояние" между запусками программы.

"""


# Определение базового класса Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод для издавания звуков, который будет переопределяться в подклассах
    def make_sound(self):
        pass

    # Общий метод для всех животных - еда
    def eat(self):
        print(self.name + " ест.")


# Создание подкласса Bird, наследующего от Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    # Переопределение метода make_sound для птиц
    def make_sound(self):
        print(self.name + " говорит чирик.")


# Создание подкласса Mammal, наследующего от Animal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    # Переопределение метода make_sound для млекопитающих
    def make_sound(self):
        print(self.name + " говорит грр.")


# Создание подкласса Reptile, наследующего от Animal
class Reptile(Animal):
    def __init__(self, name, age, scales_color):
        super().__init__(name, age)
        self.scales_color = scales_color

    # Переопределение метода make_sound для рептилий
    def make_sound(self):
        print(self.name + " говорит шшш.")


# Функция, демонстрирующая полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Создание объектов животных разных классов
bird = Bird("Твитик", 2, "30 см")
mammal = Mammal("Пушистик", 4, "Коричневый")
reptile = Reptile("Скользящий", 5, "Зеленый")

# Список животных
animals = [bird, mammal, reptile]

# Вызов функции, демонстрирующей полиморфизм
animal_sound(animals)

