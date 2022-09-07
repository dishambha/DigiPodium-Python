data = ""#global variable (it can only be displayed in function but can't be changed)
def data_appender(s):
    global data # this line tells data_appender that we have a global variable data
    if len(s)>0:
        data += s
#call
data_appender("hello ")
data_appender("world ")
data_appender("this is a simple function ")
data_appender("pahale istamal karein fir vishwash karein ")
#variable defined in side the function can not be used outside the function
#to use the variable outside the function it should be declared out side the function
print(data)

