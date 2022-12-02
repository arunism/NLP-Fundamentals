import numpy as np
from scipy import spatial

glove_filepath = 'glove.6B.50d.txt'

embeddings_dict = {}
with open(glove_filepath, 'r') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector

# Find similar Vectors
def find_similar_vectors(inputs):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embeddings_dict[inputs]))

# Example:
find_similar_vectors('king')[:5]    # Get top 5 similar words
