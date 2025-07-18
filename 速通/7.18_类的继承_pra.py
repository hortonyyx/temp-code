class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Dog 继承自 Animal
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):  # 重写父类方法
        print(f"{self.name} barks.")

my_dog = Dog("Buddy")
my_dog.make_sound()  # 输出: Buddy barks.