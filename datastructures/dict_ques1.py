contacts ={
    "Dishambha":{
        "name": "dishambha",
        "contact": 9369879498
    },
    "gaurvanvita":{
        "name": 'gaurvanvita',
        "contact": 9044388808

    },
    "mummy":{
        "name": "anamika",
        "contact": 7007986810

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

   

