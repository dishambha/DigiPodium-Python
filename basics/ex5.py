amount =float(input("Enter an amount"))
if amount <=1500:
    print (f"pay the complete amount{amount}")
else :
    discount = amount*0.15
    value = amount-discount
    print (f"The payable amount is{value} and your discount is {discount}")