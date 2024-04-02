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
        self.type_of_animal = 'Птица'

    # Переопределение метода make_sound для птиц
    def make_sound(self):
        print(self.name + " говорит чирик.")


# Создание подкласса Mammal, наследующего от Animal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color
        self.type_of_animal = 'Mлекопитающее'

    # Переопределение метода make_sound для млекопитающих
    def make_sound(self):
        print(self.name + " говорит грр.")


# Создание подкласса Reptile, наследующего от Animal
class Reptile(Animal):
    def __init__(self, name, age, scales_color):
        super().__init__(name, age)
        self.scales_color = scales_color
        self.type_of_animal = 'Рептилия'

    # Переопределение метода make_sound для рептилий
    def make_sound(self):
        print(self.name + " говорит шшш.")


# Функция, демонстрирующая полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Класс Zoo, использующий композицию для учета животных и сотрудников
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    # Метод для добавления животных в зоопарк
    def add_animal(self, animal):
        self.animals.append(animal)

    # Метод для добавления сотрудника в зоопарк
    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    # Вывод информации о животных в зоопарке
    def display_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name}, это {animal.type_of_animal}")

    # Вывод информации о сотрудниках зоопарка
    def display_staff(self):
        print("Сотрудники зоопарка:")
        for staff in self.staff:
            print(f"- {staff.name}, это {staff.profession}")

# Класс ZooKeeper - ухаживает за животными Смотритель зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.profession = 'Смотритель зоопарка'

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

# Класс Veterinarian - врач, лечит животных
class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.profession = 'Ветеринар'

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Создание экземпляра зоопарка
zoo = Zoo()

# Создание объектов животных разных классов
bird = Bird("Твитик", 2, "30 см")
mammal = Mammal("Пушистик", 4, "Коричневый")
reptile = Reptile("Скользящий", 5, "Зеленый")

# Добавление животных в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Создание сотрудников и добавление в зоопарк
zookeeper = ZooKeeper("Том")
veterinarian = Veterinarian("Эмили")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Список животных
animals = [bird, mammal, reptile]
# Вызов функции, демонстрирующей полиморфизм
animal_sound(animals)

# Демонстрация работы с зоопарком
zoo.display_animals()
zoo.display_staff()

# Сотрудники выполняют свою работу
zookeeper.feed_animal(bird)
veterinarian.heal_animal(reptile)
