# keywords arguments -kwargs

def saveInfo(file = "info.txt",**kwargs):
    with open(file,"a")as f:
        for k,v in kwargs.items():
            f.write(f"{k}->{v}\n")

saveInfo(mobile="motorola",prize=20000,expiry = "2023",features="kuch khas nahi")
