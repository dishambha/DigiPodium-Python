#endswith

file =input("Enter File name: ")

if file.endswith(".png"):
    print("its a png file")
elif file.endswith(".jpg"):
    print("its a jpg file")
elif file.endswith(".docs"):
    print("its a word file")
elif file.endswith(".py") or file.endswith(".ipynb"):
    print("its a python file")
else:
    print("unidentified file")
