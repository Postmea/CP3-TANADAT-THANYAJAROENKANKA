class Animal():
    def eat(self):
        print("Eating !!")

class Cat(Animal):
    name = ""
    def setName(self,text):
        self.name = text
    def eat(self):
        print(f"{cat1.name} Eating by mouth !!")

cat1 = Cat()
cat1.setName("Mee")
print(cat1.name)
cat1.eat()