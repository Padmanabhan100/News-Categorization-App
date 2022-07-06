# Import the necessary libraries
import streamlit as st
from datapipeline import DataPipeline

st.set_page_config("NEWS📰 TYPE CATEGORIZATION APP🚀🚀")

st.markdown("<h1 style='text-align: center;'>News Categorization App🚀🚀</h1>", unsafe_allow_html=True)

st.image('images/bbc_news.jpg')

st.write("\n",key=555)

article = st.text_input("ENTER YOUR NEWS ARTICLES HERE👇👇 ",key=111)

st.write("\n",key=333)

st.markdown("As this model is trained on BBC News Data, please try to use the news articles from <a href='https://www.bbc.com'>their website</a> for better experience", unsafe_allow_html=True)
st.markdown("You can check the model creation✨ and model training🚀 part by clicking <a href='https://www.kaggle.com/code/padmanabhanporaiyar/news-categorization-all-types-of-clustering/notebook'>here</a>😊", unsafe_allow_html=True)


# If user enters the article
if article:
   # Define a datapipeline instance
   data_pipe = DataPipeline("model_dir",article)
   # Clean the text
   clean_article = data_pipe.clean_text()
   # Vectorize the text
   vectorized_article = data_pipe.vectorize_text(clean_article)
   # Reduce the dimensions of sparse vector
   reduced_article = data_pipe.dimension_reduction(vectorized_article)
   # Predict the news category
   predicted_category = data_pipe.predict(reduced_article)
   # Print the category 
   st.title(f"This news article belongs to {predicted_category} Category✨")

    # Some basic messages
   st.markdown("This app classifies the articles in 5 categories:", unsafe_allow_html=True)
   st.markdown("1. Business💸", unsafe_allow_html=True)
   st.markdown("2. Politics👑", unsafe_allow_html=True)
   st.markdown("3. Technology🤖", unsafe_allow_html=True)
   st.markdown("4. Entertainment🎥", unsafe_allow_html=True)
   st.markdown("5. Sports⚽", unsafe_allow_html=True)
   st.markdown("Thank you for visiting, I hope you liked it !❤️", unsafe_allow_html=True)
   