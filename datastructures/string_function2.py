#string validation functions
value = input("ENTER SOMETHING:")

#test
if value.isnumeric():
    print("ONLY NUMBER",value.isnumeric())
if value.isalpha():
    print("ONLY ALPHABETS",value.isalpha())
if value.isalnum():
    print("ALPHABETS AND NUMBERS",value.isalnum())
if value.isspace():
    print("ONLY SPACES",value.isspace())
if value.isupper():
    print("UPPER CASE ALPHABETS",value.isupper())
if value.islower():
    print("Lowercase Alphabets",value.islower())
