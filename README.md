### Software And Tools Requirements

1. [Github Account](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

# Project and Dataset overview
* This project aims to develop a fake news classifier that can determine the reliability of a news article based on its headline. The classifier uses Natural Language Processing (NLP) techniques to preprocess the text and machine learning algorithms to build the model.

* To preprocess the text data, we used the re and NLTK libraries to fetch stop words and perform lemmatization. We also used the sklearn library to vectorize the words in the sentences, which is a technique to convert the text data into numerical features that can be used for machine learning.

* The model was then trained on a dataset of labeled news articles, where each article was labeled as either reliable or unreliable. We used the Multinomial Naive Bayes algorithm to train the model, which is a popular algorithm for text classification tasks.

* After training the model, we evaluated its performance using metrics such as accuracy, precision, and recall. The model achieved an accuracy of approximately 95.09%, which suggests that it is able to effectively classify news articles as reliable or unreliable based on their headlines.

- Overall, this fake news classifier can be a useful tool for anyone who wants to quickly assess the reliability of a news article. The code for this project is available on Github for anyone who wants to use or further develop the model.

## Working model 
Giving the input- 15 Civilians Killed In Single US Airstrike Have Been Identified
![](https://github.com/Lak2k1/fkpred/blob/main/1.gif)


Giving the input- Jackie Mason: Hollywood Would Love Trump if He Bombed North Korea over Lack of Trans Bathrooms (Exclusive Video) - Breitbart


![](https://github.com/Lak2k1/fkpred/blob/main/2.gif)
