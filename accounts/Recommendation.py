from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd



songs = pd.read_csv('Songs.csv', engine='python')
songs.head()

genre_labels = set()
for s in songs['genre'].str.split(',').values:
    genre_labels = genre_labels.union(set(s))


# Break up the big genre string into a string array
songs['genre'] = songs['genre'].str.split(',')
# Convert genres to string value
songs['genre'] = songs['genre'].fillna("").astype('str')


tf = TfidfVectorizer()
tfidf_matrix = tf.fit_transform(songs['genre'])
tfidf_matrix

# In[46]:


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim[:4, :4]

# In[68]:


# Build a 1-dimensional array with songs name
titles = songs['song_name']
indices = pd.Series(songs.index, index=songs['song_name'])


# In[67]:


def genre_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    songs_indices = [i[0] for i in sim_scores]
    return titles.iloc[songs_indices]
