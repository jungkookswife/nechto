class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "РРР" # выводит напрямую в консоль
         # ?

class Cat(Pet):
    def speak(self):
        return "Мяу" # возвращает как результат
         # ?

class Fox(Pet):
    def speak(self):
        return "Фыр-фыр" # возвращает как результат
         # ?

class Hybrid(Cat, Fox):
    pass

pet1 = Pet("Питомец")
print(pet1.speak())

cat1 = Cat("Кошка")
print(cat1.speak())

fox1 = Fox("Лиса")
print(fox1.speak())

hybrid1 = Hybrid("Гибрид")
print(hybrid1.speak()) # фыр фыр