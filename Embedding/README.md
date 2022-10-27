# Embedding

Word embedding is a technique of representing individual words as a vector of numerical vectors in a predefined
vector space. Each word is mapped to a vector and the vector representations for words having same meaning are
similar.

<p align="center">
    <img src="./../Assets/embedding/embedding.jpg"><br/>
    <a href="https://www.researchgate.net/publication/361134482_A_Survey_on_Sentence_Embedding_Models_Performance_for_Patent_Analysis/figures?lo=1"><i>[Image Source]</i></a>
</p>


- ### [Bag of Words](https://github.com/arunism/NLP-Fundamentals/blob/master/Embedding/bow.ipynb)

    Bag of Words is the simplest form of word embedding. Bag of words models encode every word in the vocabulary
    as one-hot-encoded vector. The process for Bag of Words goes through the following steps:
    1. Construct a vocabulary of words.
    2. Construct a vector of dimension *d* (*d* being the vocabulary size). Each index/dimension of the vector
       corresponds to a unique word in the vocabulary. The value in each shell of the vector represents the number
       of times the word with that index occurs in the corpus.
    
    **Drawbacks of Bag-of-Words:**
    - Vector length is insanely large for large corpus.
    - BoW results to sparse matrix, which is what we would like to avoid.
    - Retains no information about grammar and ordering of words in a corpus.

    <p align="center">
      <img src="./../Assets/embedding/bow.jpg"><br/>
    </p>


## References

1. [A Survey on Sentence Embedding Models Performance for Patent Analysis](https://arxiv.org/abs/2206.02690)
2. [Apply a Simple Bag-of-Words Approach](https://openclassrooms.com/en/courses/6532301-introduction-to-natural-language-processing/6980811-apply-a-simple-bag-of-words-approach)
