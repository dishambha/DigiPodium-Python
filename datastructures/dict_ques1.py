contacts ={
    "Dishambha":{
        "name": "dishambha",
        "contact": 9262425724
    },
    "gaurvanvita":{
        "name": 'gaurvanvita',
        "contact": 7014262526

    },
    "mummy":{
        "name": "anamika",
        "contact": 8163490165

    }
}
person = (input("enter name of the person"))
if person in contacts:
    print("contact no is",contacts[person]["contact"])
else:
    print("add the contact")

newn =input("enter the name of the person")
newc =float(input("entertne no"))

contacts =[newn] = newc

   

