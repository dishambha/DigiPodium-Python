
msg = input("ENTER THE sentence=>")
new_msg = msg
for vowel in "aeiou":
    new_msg=(new_msg.lower().replace(vowel,""))
#new_msg = msg
print(msg)
print(new_msg)
