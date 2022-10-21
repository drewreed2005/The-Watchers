from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_alarm import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/alarms')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class AlarmsAPI:
    # not implemented
    class _Create(Resource):
        def post(self, alarm):
            pass
            
    # getAlarms()
    class _Read(Resource):
        def get(self):
            return jsonify(getAlarms())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getAlarms(id))

    # getRandomJoke()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomAlarm())
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countAlarms()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addJokeHaHa
    class _UpdateLike(Resource):
        def put(self, id):
            addAlarmVote(id)
            return jsonify(getAlarms(id))

    # put method: addJokeBooHoo
    class _UpdateDislike(Resource):
        def put(self, id):
            addAlarmDislike(id)
            return jsonify(getAlarms(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:alarm>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateLike, '/like/<int:id>')
    api.add_resource(_UpdateDislike, '/dislike/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'http://workwatch.nighthawkcodescrums.gq/' # run from web
    url = server + "/api/alarms"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read joke by id
        ) 
    responses.append(
        requests.put(url+"/like/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/dislike/"+num) # add to jeer count
        ) 

    # obtain a random joke
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")