# variable arguments - args
# keywords arguments -kwargs

def total(*values):
    t=0
    for i in values:
        if isinstance(i,(int,float)):
            t += i 
    return t
o = total(1,5,9,9,7)
print(o)
o = total(1,5,9,9,7,7464,5653,15453627,9,"j")
print(o)
