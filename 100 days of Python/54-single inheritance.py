class Animal:
    def __init__(self, name,specie):
        self.name = name
        self.specie = specie
    def sound(self):
        print("This Sound made by the cat")

class cat (Animal):
    def __init__(self,name,breed):
        Animal.__init__(self, name, specie="cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meow!")

d = cat("Cat", "persian")
d.make_sound()

a = Animal("cat", "Cat")
a.sound()
