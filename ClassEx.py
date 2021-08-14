class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print(f"Added to {self.name} {self.lastName}'s cart")

customer1 = Customer()
customer1.name = "Post"
customer1.lastName = "PK"
customer1.addCart()

customer2 = Customer()
customer2.name = "Jame"
customer2.lastName = "Park"
customer2.addCart()

print(customer1)
print(customer2)

