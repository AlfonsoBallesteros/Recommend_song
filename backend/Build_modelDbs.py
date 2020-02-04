# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import time
from sklearn.externals import joblib
import Recommenders as Recommenders
import Evaluations as Evaluation


client = MongoClient()
db = client['songnify']
collection = db['data']

data = collection.find({})
song_df = pd.DataFrame(data)
print(song_df.head(100))
print(type(song_df))


train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
print(type(train_data))

model1 = Recommenders.popularity_recommender_py()
model1.create(train_data, 'user_id', 'song')

users = song_df['user_id'].unique()
print(users)

user_id = users[5]
print(user_id)
model1.recommend(user_id)


joblib.dump(model1, 'model_1.pkl')

model2 = Recommenders.item_similarity_recommender_py()
model2.create(train_data, 'user_id', 'song')
print(train_data)

user_id = users[5]
print(type(user_id))
print(user_id)
user_items = model2.get_user_items(user_id)
#
print("------------------------------------------------------------------------------------")
print("Training data songs for the user userid: %s:" % user_id)
print("------------------------------------------------------------------------------------")

for user_item in user_items:
    print(user_item)

print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")

#Recommend songs for the user using personalized model
model2.recommend(user_id)

model2.get_similar_items(['U Smile - Justin Bieber'])

song = 'Yellow - Coldplay'
###Fill in the code here
model2.get_similar_items([song])

joblib.dump(model2, 'model_2.pkl')