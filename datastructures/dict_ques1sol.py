contacts = {
    "emergency": 101,
    "police" : 100
}

while True:
    print("# options ")
    print("search person")
    print("view all")
    print("exit")
    ans= input("enter a numper")
    if ans == "1":
        name = input("enter the person's name : ")
        if name in contacts:
            print(f" {name} => {contacts[name]}")
        else:
            print(f"Not found , would you like to add the {name}s' number?")
            number = input(f"enter number for {name} =>")
            contacts[name] = number
            print("details added")
    elif ans =="2":
        for name, number in contacts.items():
            print(f"  {name} => {number}")
    elif ans == "2":
        print("BYE")
        break
    else:
        print(" X wrong input X")
       