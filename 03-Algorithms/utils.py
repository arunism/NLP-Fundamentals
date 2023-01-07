import random
from nltk.corpus import wordnet
from nltk.corpus import stopwords


class EasyDataAugmentation:
    def __init__(self) -> None:
        self.stop_words = set(stopwords.words('english'))
    
    def get_synonyms(self, word):
        synonyms = set()
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonym = l.name().replace("_", " ").replace("-", " ").lower()
                synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
                synonyms.add(synonym) 
        if word in synonyms:
            synonyms.remove(word)
        return list(synonyms)

    def synonym_replacement(self, words, n):
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
            if num_replaced >= n: #only replace up to n words
                break
        return ' '.join(words)
    
    def random_deletion(self, words, p):
        words = words.split()
        if len(words) == 1:    # obviously, if there's only one word, don't delete it
            return words
        new_words = []   # randomly delete words with probability p
        for word in words:
            r = random.uniform(0, 1)
            if r > p:
                new_words.append(word)
        if len(new_words) == 0:    # if you end up deleting all words, just return a random word
            rand_int = random.randint(0, len(words)-1)
            return [words[rand_int]]
        return ' '.join(new_words)
