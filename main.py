import gensim.downloader as api
import random

def main():
    print("Loading the word vectors")
    word_vectors = api.load("glove-twitter-25")
    print("Done")
    
    random_word = random.choice(list(word_vectors.key_to_index.keys()))
    print("The random word is: ", random_word)
    
    '''
    user_input = input("enter word: ")
    try:
        print(model.wv.similarity(random_word, user_input))
    except:
        print("word dont exsists")
    '''
    
if __name__ == "__main__":
    main()
