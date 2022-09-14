class cat:
    #attributes,fields,class member,properties
    color = "black"
    breed = "persian"
    age = 2

    #method/function
    def eat(self):
        print("cat is eating")

    def play(self):
        print("cat is playing")

    def description(self):
        print(f"cat is {self.age} years old")
        print(f"cat is {self.color} years old")
        print(f"cat is {self.breed} years old")

#object 
tom = cat() #()is to call the constructor the class

tom.eat()
tom.play()
tom.description() 








    