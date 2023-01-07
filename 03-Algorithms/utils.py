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
    