from helper import read
data = read('pride_n_prejudice.txt')
def word_counter(data):
    
    count =data.count("and")
    return count
print(word_counter(data))

        
