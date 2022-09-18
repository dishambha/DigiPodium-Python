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
        print(f"cat is {self.color} is color")
        print(f"cat is {self.breed} breed")

#object 
tom = cat() #()is to call the constructor the class

tom.eat()
tom.play()
tom.description()

tom.age = 3
tom.breed = "british shorthair"
tom.color = "grey"
tom.description()








    