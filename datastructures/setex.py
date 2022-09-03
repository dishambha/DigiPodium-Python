dry_fruits= {"dates ","almond","walnut","cashew"}
fruits ={"apple","mango","grapes","papaya"}

all_fruits = fruits | dry_fruits
print(dry_fruits)
print(fruits)
print(all_fruits)
#if any element is common the true
ans = dry_fruits.isdisjoint(fruits)
print(ans)
#if all elements of a set is present in another
ans = dry_fruits.issuperset(all_fruits)
print(ans)

ans = dry_fruits.issuperset({"apple","mango"})
print(ans)
