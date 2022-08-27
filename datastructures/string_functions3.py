#string validation 

value = input("ENTER THE GUEST NAME:")
#startswith
if value.startswith("Mr."):
    print("WELLCOM SIR")
elif value.startswith("Ms."):
    print("WELLcom ma'am")
elif value.startswith("Dr."):
    print("WELLCON DOCTOR")
else :
    print("YOU ARE NOT INVITED")

