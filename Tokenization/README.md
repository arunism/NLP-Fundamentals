# Tokenization

Tokenization is one of the first steps in NLP pipeline.
It is a technique to split a sentence, phrase, paragraph or an entire document to smaller units.
These smaller units are called tokens. Tokens must not always be words. They can be either
symbols and letters (., !, a, z, ...) or sentences or any other forms of text.

> The program works well with python version >=3.8.0.
> Make sure the requirements mentioned here are satisfied,
> or the result may not be as expected.

## Methods Included

- [NLTK](https://github.com/arunism/NLP-Fundamentals/blob/master/Tokenization/nltk.ipynb)
    
    This module is used for statistical natural language processing. It consists of module called `tokenize`
    with several methods that aids in splitting text to tokens like: `word_tokenize`, `sent_tokenize`,
    `wordpunct_tokenize`, `WhitespaceTokenizer`.

    <p align="center">
        <img src="./assets/nltk.jpg"><br/>
        <a href="https://udemy.com/course/python-for-data-science-and-machine-learning-bootcamp"><i>Image source</i><a/>
    <p/>


- [Spacy](https://github.com/arunism/NLP-Fundamentals/blob/master/Tokenization/spacy.ipynb)
    
    In Spacy, the process of tokenizing a text into segments of words and punctuation is done in various steps.
    It processes the text from left to right.

    - First, the tokenizer split the text on whitespace similar to the split() function.
    - Then the tokenizer checks whether the substring matches the tokenizer exception rules. For example,
      “don’t” does not contain whitespace, but should be split into two tokens, “do” and “n’t”, while “U.K.”
      should always remain one token.
    - Next, it checks for a prefix, suffix, or infix in a substring, these include commas, periods, hyphens, or quotes.
      If it matches, the substring is split into two tokens.

    <p align="center">
      <img src="./assets/spacy.jpg"><br/>
      <a href="https://machinelearningknowledge.ai/complete-guide-to-spacy-tokenizer-with-examples/"><i>Source</i><a/>
    <p/>


## References

1. [NLTK Tokenizer Package Documentation](https://www.nltk.org/api/nltk.tokenize.html)
2. [NLTK Tokenize – Complete Tutorial for Beginners](https://machinelearningknowledge.ai/nltk-tokenizer-tutorial-with-word_tokenize-sent_tokenize-whitespacetokenizer-wordpuncttokenizer/)
3. [Python for Data Science and Machine Learning Bootcamp](https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/)
4. [Spacy Tokenization Documentation](https://spacy.io/usage/linguistic-features#tokenization)
5. [Complete Guide to Spacy Tokenizer with Examples](https://machinelearningknowledge.ai/complete-guide-to-spacy-tokenizer-with-examples/)
6. [TorchText Tokenizer Documentation](https://pytorch.org/text/stable/data_utils.html)
