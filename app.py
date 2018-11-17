from flask import Flask, jsonify,json, render_template, flash, redirect, request, url_for, session, logging
from data import UserData

app = Flask(__name__)
Rides = UserData().Rides()
usersdetails = UserData().users()

#NOW I  ADDED THE FUNCTIONALTY OF ALL THE ENDPOINTS OF THE ROUTES
@app.route('/' , methods=['GET'])
def index():
    return render_template('index.html')

#user registration route
@app.route('/register',methods = ['POST'])
def register():
    return jsonify({'users': usersdetails})
    #return render_template('register.html')

#user login form......and the class
@app.route('/login', methods= ['POST'])
def login():
    return jsonify({'users': usersdetails})
    #return render_template('login.html')

#USERS ACCESS AND VIEW THEIR ACCOUNTS DETAILS(ACCOUNT PREVIEW)
@app.route('/myaccount/<string:name>',methods=['GET'])
def account(name):
    user = [userprofile for userprofile in usersdetails if userprofile['name'] == name]
    return jsonify({'userdetail' : user[0]})
    #return render_template('myaccount.html')

#THE USER CAN UPDATE HIS/HER PROFILE WITH THIS ROUTE
@app.route('/updateprofile/<string:name>', methods=['PUT','GET'])
def updateprofile(name):
    data = request.get_json()
    userupdate = [singleprofileupdate for singleprofileupdate in usersdetails if singleprofileupdate['name'] == name]
    userupdate[0]['name'] = data['name']
    return jsonify({'profileupdate' : userupdate[0]})
    #return render_template('updateprofile.html')

#===================RIDES SECTION===============================================
#ALL RIDES ARE SEEN AND AVAILABLE HERE
#ROUTES TO ACCESS THE ALL THE  RIDES AND DETAILS AND
#ACCESSING THE DATA STRUCTURE AND DISPLAYING ALL THE RIDES AVAILBLE
@app.route('/ride', methods=['GET'])
def ridesdetails():
    return jsonify({'rides': Rides})

#ACCESSING A SINGLE RIDE :::
@app.route('/ride/<string:name>', methods = ['GET'])
def oneride(name):
    rideone = [singleride for singleride in Rides if singleride['ride'] == name]
    return jsonify({'oneride' : rideone[0]})
#if what i am l ooping through(ride['ride']) is equal to ride
#then it create a new list with all the matches
#basic working

#-------confirmed route working--------------------------
#this route is supposed to add new rides into the db
@app.route('/ride', methods=['POST','GET'])
def addride():
    data = request.get_json()
    newride = { "ride" : data['ride']}
    Rides.append(newride)
    return jsonify({'rideadded': Rides})

#-------confirmed route working after debugging--------------------------
@app.route('/ride/<string:name>', methods =['PUT'])
def updateride(name):
    data = request.get_json()
    rideone = [singleride for singleride in Rides if singleride['name'] == name]
    rideupdate[0]['name'] = data['name']
    return jsonify({'language' : rideupdate[0]})

#-------confirmed   working --------------------------
@app.route('/ride/<string:name>', methods =['DELETE'])
def removeride(name):
    rideremove = [ridedelete for ridedelete in Rides if ridedelete['name'] == name]
    Rides.remove(rideremove[0])
    return jsonify({'languages' : Rides})

#USER CAN ACCESS HIS/HER REQUEST  : REJECT/ACCEPTED NOTIFUICATION HERE
@app.route('/notifications', methods=['GET'])
def notifications():
    return render_template('notifications.html')

#THIS ROUTE HAS NO ENDPOINT AND THE USER CAN ACCESS IT SINCE THE DISPLAYED INFO IS IN THE HTML
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    app.secret_key = 'key12364'
    app.run(debug= True)
