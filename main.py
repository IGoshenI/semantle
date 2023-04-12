import gensim.downloader as api
from random_word import RandomWords

def main():
    print("Loading the word vectors")
    word_vectors = api.load("word2vec-google-news-300")
    print("Done")
    
    random = RandomWords()  
    while True:
        random_word = random.get_random_word()
        if random_word in word_vectors.key_to_index.keys():
            break
    print("The random word is: ", random_word)
    
    done = False
    while not done:
        user_input = input("enter word: ")
        if user_input not in word_vectors.key_to_index.keys():
            print("given word does not exsists")
        
        similarity = word_vectors.similarity(random_word, user_input)
        print (similarity)
        
        if similarity == 1:
            done = True
    

if __name__ == "__main__":
    main()
