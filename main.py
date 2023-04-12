import gensim.downloader as api
from random_word import RandomWords

def generate_random_word(model):
    random = RandomWords()  
    while True:
        random_word = random.get_random_word()
        if random_word in model.key_to_index.keys():
            break
    return random_word


def main():
    print("Loading the word vectors")
    model = api.load("word2vec-google-news-300")
    print("Done\n")
    
    random_word = generate_random_word(model)
    print("The random word is: ", random_word) # for debugging, remove later
    
    done = False
    while not done:
        user_input = input("enter word: ")
        word_not_exists = user_input not in model.key_to_index.keys()
        if word_not_exists:
            print("given word does not exsists, try another word.")
            continue
        
        similarity = model.similarity(random_word, user_input)
        print (similarity)
        
        if similarity == 1:
            done = True
    

if __name__ == "__main__":
    main()
