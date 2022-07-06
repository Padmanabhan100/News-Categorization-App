# For NLP(text cleaning)
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# To load the model
import pickle

# To supress warnings
import warnings
warnings.filterwarnings("ignore")

# Download the nltk corpus
nltk.download("stopwords")

class DataPipeline:
    def __init__(self,model_path,input_text):
        self.model_path = model_path
        self.input_text = input_text
        self.ps = PorterStemmer()
        self.labels_map = {0:"Sports",1:"Technology",2:"Business",3:"Entertainment",4:"Politics"}

    def clean_text(self):
        # Replace the end lines <\n>
        article = self.input_text.replace("\\n",'')
        # Remove all excepth the alphabets
        article = re.sub("[^a-zA-Z]",' ', article)
        # Lower all the aplhabets
        article = article.lower()
        # Split the article on spaces, returning a list of words
        words = article.split()
        # Remove stopwords
        clean_article = [self.ps.stem(word) for word in words if not word in stopwords.words("english")]
        # Join clean words
        clean_article = " ".join(clean_article)
        # return the clean text
        return [clean_article]


    def vectorize_text(self,clean_text):
        # Load the vectorizer
        tfidf = pickle.load(open("vectorizer/vectorizer.pickle",'rb'))
        # Transform the text
        article_vector = tfidf.transform(list(clean_text))
        # Return the clean article
        return article_vector

    def dimension_reduction(self,article_vector):
        # Load the dimension reduction object
        svd = pickle.load(open("dimension reduction/svd.p",'rb'))
        # Transform the sparse matrix
        article_reduced = svd.transform(article_vector)
        print(article_reduced)
        # Return the reduced vector
        return article_reduced


    def predict(self, article_reduced):
        # Load the model
        model = pickle.load(open("model_dir/kmeans_model.sav",'rb'))
        # Make predictions
        prediction = model.predict(article_reduced[0].reshape(1,-1))
        # Map the integer label with the text
        predicted_label = self.labels_map[prediction[0]]
        # Return the predicted labels
        return predicted_label