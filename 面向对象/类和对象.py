class animals:
    def __init__(self,name,species,sound):
        self.name = name
        self.species = species
        self.sound = sound
    def make_soung(self):
        print(f"{self.species} {self.name} make sound like {self.sound}")
    def __del__(self):
        print(f'{self.species} {self.name} has been deleted!')

animal_1 = animals('pupu','donkey','muuuuu')
animal_2 = animals('timmy','cat','miaooooo')
animal_3 = animals('dindin','ox','mermermer')

print(animal_1.name)
print(animal_1.species)
print(animal_1.sound)

animal_1.make_soung()
animal_2.make_soung()
animal_3.make_soung()


#析构函数：就是当删除实例的时候，调用这个函数提醒一下
del animal_2