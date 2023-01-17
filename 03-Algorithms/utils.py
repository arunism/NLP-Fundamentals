import re
import nltk
import random
from nltk.corpus import wordnet
from nltk.corpus import stopwords


def clean(sentence):
    sentence = re.sub(r'[?|$|.|!]',r'', sentence.lower())
    return  re.sub(r'[.|,|)|(|\|/]',r' ', sentence)


class EasyDataAugmentation:
    def __init__(self) -> None:
        # nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
    
    def get_synonyms(self, word):
        # nltk.download('wordnet')
        synonyms = set()
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonym = l.name().replace("_", " ").replace("-", " ").lower()
                synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
                synonyms.add(synonym) 
        if word in synonyms:
            synonyms.remove(word)
        return list(synonyms)

    def synonym_replacement(self, words, n=2):
        words = words.split()
        random_word_list = list(set([word for word in words if word not in self.stop_words]))
        random.shuffle(random_word_list)
        num_replaced = 0
        for random_word in random_word_list:
            synonyms = self.get_synonyms(random_word)
            if len(synonyms) >= 1:
                synonym = random.choice(list(synonyms))
                words = [synonym if word == random_word else word for word in words]
                num_replaced += 1
            if num_replaced >= n: # Replace n words at max
                break
        return ' '.join(words)

    def random_insertion(self, words, n=2):
        words = words.split()
        new_words = words.copy()
        for _ in range(n):
            self.add_word(new_words)
        return ' '.join(new_words)
    
    def random_deletion(self, words, n=2):
        words = words.split()
        if len(words) == 1:    # If there's only one word, don't delete it
            return words
        new_words = []   # Randomly delete words with probability p
        for word in words:
            r = random.uniform(0, 1)
            if r > n:
                new_words.append(word)
        if len(new_words) == 0:    # if you end up deleting all words, just return a random word
            rand_int = random.randint(0, len(words)-1)
            return [words[rand_int]]
        return ' '.join(new_words)

    def swap_word(self, new_words):
        random_idx_1 = random.randint(0, len(new_words)-1)
        random_idx_2 = random_idx_1
        counter = 0
        while random_idx_2 == random_idx_1:
            random_idx_2 = random.randint(0, len(new_words)-1)
            counter += 1
            if counter > 3:
                return new_words
        new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1] 
        return new_words

    def add_word(self, new_words):
        synonyms = []
        counter = 0
        while len(synonyms) < 1:
            random_word = new_words[random.randint(0, len(new_words)-1)]
            synonyms = self.get_synonyms(random_word)
            counter += 1
            if counter >= 10:
                return
        random_synonym = synonyms[0]
        random_idx = random.randint(0, len(new_words)-1)
        new_words.insert(random_idx, random_synonym)
    
    def random_swap(self, words, n=2):
        words = words.split()
        new_words = words.copy()
        for _ in range(n):    # n is the number of words to be swapped
            new_words = self.swap_word(new_words)
        return ' '.join(new_words)
