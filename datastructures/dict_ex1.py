#info = ["Mistborn","The final Empire","Brandon Sandors","tor.com",2099,2002]
info_dict = {
    "SERIES":"Mistborn",
    "TITLE":"The Final Empire",
    "AUTHOR":"Brandon Sandors",
    "PUBLISHER":"tor.com",
    "PRICE":2099,
    "YEAR":2002
}
print(info_dict)
print(info_dict.keys())
print(info_dict.values())
print(info_dict["SERIES"])
print(info_dict.get("AUTHOR")) 

#update existind value
info_dict["PRICE"]= 599
print(info_dict)

# adding a new key value
info_dict["RATING"] = 10
print(info_dict)
