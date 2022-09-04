# nested dictonary

emps = {
    "chandu":{
        "name ": "chandu sharma",
        "salary": 15000,
        "designation": "foreman"
    },
    "rohit":{
        "name": "rohit kumar singh",
        "salary": 18000,
        "designation": "assistant 2",
        "manager": "ravi prakash"
    },
    "bhanu":{
        "name": "bhanu pratap",
        "salary": 1000,
        "designation": "system officer"
    }
}

print("designation is :",emps["chandu"]["designation"])

for key,data in emps.items():
    print(key," ||")
    for k,v in data.items():
        print(k,v)
    print("--"*10)