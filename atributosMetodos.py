class Person:
    species="Humano"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy=100 #protected attribute
        self.__password="12345" #private attribute

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    def _waste_energy(self, amount):
        self._energy-=amount
        if self._energy<0:
            self._energy=0
        return self._energy
    def __generate_password(self):
        return f"##{self.name}{self.age}##"
person1 = Person("Adan", 47)
print(person1.introduce())
print(person1.species)
print(person1._waste_energy(30))
print(person1._Person__password)
print(person1._Person__generate_password())
