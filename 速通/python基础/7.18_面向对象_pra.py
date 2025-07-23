#
# class Dog:
#     species = "Canine"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} is barking!")
#
# dog1 = Dog("Happy", 3)
# dog2 = Dog("Wangcai", 4)
#
# print(dog1.species)
# print(dog2.name)
# print(Dog.species)
#
# dog1.bark()


class Animal:
    def __init__(self, name, age, specie, sound):
        self.name = name
        self.age = age
        self.specie = specie
        self.sound = sound
    def make_sound(self):
        print(f"{self.specie}的{self.name}发出了“{self.sound}”的叫声")

    # 析构函数：删除时还需要操作的
    def __del__(self):
        print(f"{self.specie}的{self.name}被删除了")


dog1 = Animal("旺财", 3, "dog", "汪汪")
rabbit1 = Animal("跳跳", 1, "rabbit", "唧唧")
horse1 = Animal("奔奔", 2, "horse", "嘶嘶")

del horse1

#这里程序结束自动删除时会触发所有del


#获取实例属性和检查实例是否存在某个属性

# print(getattr(dog1, "sound"))
# print(hasattr(rabbit1, "color"))
# setattr(rabbit1, "color", "red")
# print(getattr(rabbit1, "color"))
# delattr(rabbit1, "color")
# print(hasattr(rabbit1, "color"))



