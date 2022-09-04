from pprint import pprint
movies ={}

#adding a single value
movies["sholey"] = "2 frns fight with a deciot"
movies["inception"] = "no summary available"

#adding multiple values 
movies.update(
    ironman="a man builds a iron suit in afganistan",
    hulk="a man becomes a monster because of an experiment",
    batman="a man who becomes a hero at night"

)
#remove
movies.pop("sholey")

#update
movies["inception"]= "dream within dream with recursion logic"

#update 2
movies["batman"] += " and fights crime"
pprint(movies)
