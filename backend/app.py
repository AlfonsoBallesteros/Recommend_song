# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS 
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from pymongo import MongoClient
import pandas as pd
import Recommenders as Recommenders
import uuid

app = Flask(__name__)
CORS(app)

'''
model_1 = joblib.load('model_1.pkl')

model_2 = joblib.load('model_2.pkl')
'''
client = MongoClient()
db = client['songnify']
collection = db['data']


@app.route('/populate/song', methods=['GET'])
def list_populate_song():
    
    #populate = collection.find({}, {'_id': False}).sort("listen_count", -1)
    populate = collection.aggregate([
            {"$group": {
                    "_id": {"id":"$song_id", "title": "$title", "release": "$release", "artist_name": "$artist_name", "year": "$year", "song": "$song"},
                    "count": {"$sum": 1}
                    }
            },{"$sort":{
                    "count": -1
                    }
                }
            ])
    
    songs = pd.DataFrame(populate)
    data_song = songs.to_json(orient="records")
    return (data_song)

@app.route('/build-model/user-new', methods=['POST'])
def build_modelUser_new():
    content = request.get_json()
    
    like_song = collection.insert_many(content)
    
    user_id = (content[0]['user_id'])
    train_model = build_model2(user_id)
    '''
    if(train_model):
        model_2 = joblib.load('model_2.pkl')
        recomend_model2 = model_2.recommend(user_id)
        res = recomend_model2.to_json(orient="records")
        return (res)
    else:
        return jsonify(train_model)
        '''
    return jsonify({ 'ok': train_model})

@app.route('/build-model/user-old', methods=['POST'])
def build_modelUser_old():
    content = request.get_json()
    find_song = collection.find_one_and_update({"song_id": content['song_id'], "user_id": content['user_id']}, {'$inc': {'listen_count': 1}})
    user_id = (content['user_id'])
    train_model = build_model2(user_id)
    #find_song_data = pd.DataFrame(list(find_song))
    #respo = find_song_data.to_json(orient="records")
    #print(find_song_data)
    return jsonify({ 'ok': train_model})

@app.route('/recommend/new', methods=['POST'])
def recomend_model2():
    content = request.get_json()
    model_2 = joblib.load('model_2.pkl')
    recomend_model2 = model_2.recommend(content['user_id'])
    res = recomend_model2.to_json(orient="records")
    return (res)

@app.route('/recommend/old', methods=['POST'])
def recomend_model1():
    content = request.get_json()
    model_1 = joblib.load('model_1.pkl')
    recomend_model1 = model_1.recommend(content['user_id'])
    res = recomend_model1.to_json(orient="records")
    return (res)

@app.route('/recommend/simmilar', methods=['POST'])
def recomend_simmilar():
    content = request.get_json()
    model_2 = joblib.load('model_2.pkl')
    recomend_model2 = model_2.get_similar_items([content['song']])
    res = recomend_model2.to_json(orient="records")
    return (res)
        
def build_model2(user_id):
    data = collection.find({})
    song_df = pd.DataFrame(data)
      
    print(type(song_df))
    
    train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
    
    print(type(train_data))
    
    model2 = Recommenders.item_similarity_recommender_py()
    model2.create(train_data, 'user_id', 'song')
    user_items = model2.get_user_items(user_id)
 
    joblib.dump(model2, 'model_2.pkl')
    return (True)

def build_model1(user_id):
    data = collection.find({})
    song_df = pd.DataFrame(data)
      
    print(type(song_df))
    
    train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
    
    print(type(train_data))
    
    model1 = Recommenders.popularity_recommender_py()
    model1.create(train_data, 'user_id', 'song')
 
    joblib.dump(model1, 'model_1.pkl')
    return (True)

@app.route('/all/song', methods=['GET'])
def get_allSong():
    song = collection.aggregate([
            {"$group": {
                    "_id": {"id":"$song_id", 
                            "title": "$title", 
                            "release": "$release", 
                            "artist_name": "$artist_name", 
                            "year": "$year", 
                            "song": "$song"}
                    }
                }
            ])
    song_data = pd.DataFrame(song)
    resp = song_data.to_json(orient="records")
    return (resp)

@app.route('/one/song', methods=['POST'])
def get_oneSong():
    content = request.get_json()
    
    song = collection.aggregate([
            {"$match": { "song_id":  content['song_id']}},
            {"$group": {
                    "_id": {"id":"$song_id", 
                            "title": "$title", 
                            "release": "$release", 
                            "artist_name": "$artist_name", 
                            "year": "$year", 
                            "song": "$song",
                            }
                    }
                }
            ])
    song_data = pd.DataFrame(song)
    resp = song_data.to_json(orient="records")

    return (resp)

@app.route('/find/song', methods=['POST'])
def get_findSong():
    content = request.get_json()
    
    song = collection.aggregate([
            {"$match": { "song":  content['song']}},
            {"$group": {
                    "_id": {"id":"$song_id", 
                            "title": "$title", 
                            "release": "$release", 
                            "artist_name": "$artist_name", 
                            "year": "$year", 
                            "song": "$song",
                           }
                    }
                }
            ])
    song_data = pd.DataFrame(song)
    resp = song_data.to_json(orient="records")

    return (resp)

@app.route('/user/login', methods=['POST'])
def login():
    content = request.get_json()
    
    collection = db['user']
    response = collection.find_one({'correo': content['correo']})
    
    if response:
        if (response['password'] == content['password']):
            return jsonify({'ok': True, 'user_id': response['user_id']})
        else:
            return jsonify('contraseña incorrecta')
    else:
        return jsonify('usuario incorrecto')

@app.route('/user/register', methods=['POST'])
def register():
    content = request.get_json()
    
    id = uuid.uuid4()
    user_id = id.hex
    content['user_id'] = user_id
    
    collection = db['user']
    find_user = collection.find({'correo': content['correo']}, {'_id': False}).count() > 0    
    if(find_user):
        return jsonify({'error': 'Este correo ya existe'})
    else:
        register = collection.insert_one(content)
        return jsonify({'ok': True, 'user_id': content['user_id']})
        #return jsonify({'ok':True})
    #register = collection.insert_one(content)
    
    #return jsonify(find_user)
    #jsonify({'ok': True, 'user_id': content['user_id']})

if __name__ == '__main__':
    app.debug = True
    app.run()
    