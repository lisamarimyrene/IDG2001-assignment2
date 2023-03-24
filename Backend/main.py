# Import modules
from flask import Flask, render_template, request, jsonify
import json
import html
import os
import bson

# Import files
import database
import functions
import vcard_parser

# Imported functions from files
from database import db
from database import collection
from vcard_parser import vcard_parser
# from functions import

# Set the flask app
app = Flask(__name__)

#hei

# POST /contacts endpoint
@app.route('/contacts', methods=['POST'])
def newContact():
    vcard_parser()
    with open('export.json') as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        collection.insert_many(file_data)
        response = {'message': 'Inserted many'}
        return jsonify(response)
        
    else:
        collection.insert_one(file_data)
        response = {'message': 'Inserted one'}
        return jsonify(response)
        


#GET/contacts : Finds all contacts 
@app.route('/contacts', methods=['GET'])
def getAllContacts():
 result = collection.find()
 return f' {(list(result))}'
  


#Finds one contact based off id
@app.route('/contactsid', methods=['GET'])
def getContacts():
  from bson.objectid import ObjectId
  result = collection.find_one({"_id": ObjectId("641c63f64b212cebf543eb01")})
  return f'{result}'
      


 # user_data = export.json
    # implement code to create and return user data
    # return jsonify(user)



# GET /contacts endpoint (json)
# @app.route('/contacts', methods=['GET'])
# GET /contacts/id endpoint (json)
# GET /contacts/vcard (vcard)
# GET /contacts/id/vcard (vcard)





# Hele greia er et Endpoint
# Dette er routen til Endpointet



# @app.route('/', methods=['GET'])
# # Dette er controlleren til Endpointet
#     def hello_world():
#      response = {'message': 'Hello from gruppen!'}
#      return jsonify(response)







# Just a standard if that is needed in every flask application
if __name__ == '__main__':
    app.run(port=3000)



