from helper import read
data = read('pride_n_prejudice.txt')
def word_counter(data):
    words = data.split()
    return len(words)
print(word_counter(data))