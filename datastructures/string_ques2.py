from string import ascii_lowercase
sen ="i am dishambha awasthi , i am live in lucknow dishambha"
start =0
query ="dishambha"
while True:
    idx =sen.find(query,start)
    if idx ==-1:
        break
    print(f"{query} at {idx}")
    start = idx+1