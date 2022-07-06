# News Categorization App🗞️

<h2>Problem Statement - </h2>

We have been given dataset of small news articles from BBC news, and we have been assigned a task to be able to successfully categorize the news articles into 5 categories- 

<ul>
<li> Sports ⚽</li>
<li> Technology 🤖</li>
<li> Business 💸</li>
<li> Entertainment 🎥</li>
<li> Politics 👑</li>
</ul>

You can find the dataset on kaggle✨ here - https://www.kaggle.com/datasets/pariza/bbc-news-summary

We have been given the labels in the kaggle dataset, but we are trying to frame an unsupervised case study to make it more intersting.

<h2> Approaching the problem statement 🚀</h2>

As we have only the text data and we have been told to categorize the news articles and we even donot have the labels for the news articles, we can say that it is a NLP
unsupervised categorization problem.

We can solve this categorization problem using clustering techniques where we can convert the text to vectors and cluster the similar vectors together and then check
which cluster belongs to which category.

<h2> Steps to solve this problem statement 🪜</h2>
<ol>
<li> <b>Clean the text data</b> 🧹</li>

By clean the text data I mean removing the stopwords and applying stemming/lemmitization.

<li> <b>Convert the clean text to vectors</b> 🔢</li>

After the cleaning process we can try to convert the clean text content to vectors. We can use any suitable method like - Bag Of Words, Word2Vec, TFIDF, Text Embeddings,etc.
In our case, we will be using the TFIDF approach


<li> <b>Dimension Reduction</b> 🥤</li>

We will use Truncated SVD to reduce the sparse TFIDF vector, to decrease the computation effort and improve latency of the algorithm.

<li> <b>Clustering</b> ✨</li>

Finally we will be training a clustering algorithm like - K-means, Gaussian Mixture Model, Hierarchical to get the clusters for categotization.

<h2> You can find the whole pre-processing and modelling in the notebook for which the link is given below - </h2>

https://www.kaggle.com/code/padmanabhanporaiyar/news-categorization-all-types-of-clustering

<h2> Deployment 🪂</h2>

This application is built using the streamlit framework which makes creating webpages extramely easy and has been deployed on heroku.

You can try using the app by following the link given below - 
https://news-categorization-app.herokuapp.com/

<h2> Here is the demo of the app in case there is some problem with heroku - 💼</h2>

![AppDemoGIF](https://user-images.githubusercontent.com/73405735/177489875-b893f661-14c7-4673-afbe-df412a422f1d.gif)
