from string import punctuation

msg ="gfyjugsuc&(73qr25#(5@*^"
for p in punctuation:
    #print(p)
    msg = msg.replace(p,"")
print(msg)
