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


- ### [TF-IDF](https://github.com/arunism/NLP-Fundamentals/blob/master/Embedding/bow.ipynb)

    In NLP an independent text entity is known as document and the collection of all these documents over the
    project space is known as corpus. TF-IDF stands for Term Frequency-Inverse Document Frequency.
    The entire technique can be studied by studying _TF_ and _IDF_ separately.

    _Term-Frequency_ is a measure of frequency of appearance of term *t* in a document *d*. In other words,
    the probability of finding term *t* in a document *d*. `Mathematically:`

    <p align="center">
      <img src="./../Assets/embedding/tf.jpg"><br/>
    </p>

    *Inverse-Document-Frequency* is a measure of inverse of probability of finding a document that contains term _t_
    in a corpus. In other words, a measure of the importance of term _t_. `Mathematically:`

    <p align="center">
      <img src="./../Assets/embedding/idf.jpg"><br/>
    </p>

    We can now compute the TF-IDF score for each word in the corpus. Words with a higher score are more important. 
    TF-IDF score is high when both IDF and TF values are high. So, TF-IDF gives more importance to words that are:
    1. More frequent in the entire corpus
    2. Rare in the corpus but frequent in the document.

    Now this TF-IDF score is used as a value for each shell of the document-term matrix, just like the frequency of
    words in case of Bag-of-Words. The formula below is used to compute TF-IDF score for each shell:

    <p align="center">
      <img src="./../Assets/embedding/tf-idf.jpg"><br/>
    </p>


## References

1. [A Survey on Sentence Embedding Models Performance for Patent Analysis](https://arxiv.org/abs/2206.02690)
2. [Apply a Simple Bag-of-Words Approach](https://openclassrooms.com/en/courses/6532301-introduction-to-natural-language-processing/6980811-apply-a-simple-bag-of-words-approach)
3. [Quick Introduction to Bag-of-Words and TF-IDF](https://www.analyticsvidhya.com/blog/2020/02/quick-introduction-bag-of-words-bow-tf-idf/)
