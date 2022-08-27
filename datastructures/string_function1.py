msg = "Journey before Destination"

#formatting function
print("Upper:",msg.upper())
print("lower:",msg.lower())
print("title:",msg.title())
print("captalize:",msg.capitalize())
print("snapcase:",msg.swapcase())
print("casefold:",msg.casefold())#same as lower

print("original:",msg)
msg = msg.upper()  #updating the msg variable to store upper cased string
print("updated:",msg)