class Person:
    species="Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def change_species(cls,new_species):
        cls.species=new_species
    @staticmethod
    def is_adult(age):
        return age >= 18
person1 = Person("Adan", 47)
person2=Person("Alexandra", 20)
print(person1.species)
print(person2.species)
#person1.change_species("Alien")
Person.change_species("Alien")
print(person1.species)
print(person2.species)

print(Person.is_adult(17))
print(person1.is_adult(person1.age))