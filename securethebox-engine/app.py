#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import time
import os
from datetime import datetime, timedelta
import requests
import json

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

"""

Kubernetes needs to be online for the engine to work

Need to fix on disconnect; there is a game of no socket data because client disconnected

Should be sending results to firebase
Client should be getting information from firebase

"""

# This is the main thread that will ccommunicate to client
def background_thread():
   check_app_status()


# check if app is online/offline
def check_app_status():
    while True:
        
        # setting sleep to 15 seconds should not cause downtime
        socketio.sleep(3)
        # count += 1
        timenow = datetime.now()
        
        try:
            auth_result = check_app_authentication(timenow)
            response = requests.request("GET", 'http://juice-shop-charles.us-west1-a.securethebox.us')
            if response.status_code == 200:
                socketio.emit('my_response', {'app_status':'online', 'api_user_login':auth_result,'startTime':str(timenow.isoformat()), 'endTime':str((timenow+timedelta(seconds=1)).isoformat()), 'title':'up'})
            else:
                socketio.emit('my_response', {'app_status':'offline', 'api_user_login':auth_result, 'startTime':str(timenow.isoformat()), 'endTime':str((timenow+timedelta(seconds=1)).isoformat()), 'title':'down'})
        except:
            socketio.emit('my_response', {'app_status':'offline', 'api_user_login':auth_result, 'startTime':str(timenow.isoformat()), 'endTime':str((timenow+timedelta(seconds=1)).isoformat()), 'title':'down'})

def create_app_user():
    print("Trying request...")
    try:
        payload = "{\"email\": \"test@securethebox.us\", \"password\": \"changemestb\"}"
        response = requests.request("POST", "http://juice-shop-charles.us-west1-a.securethebox.us/api/Users", data=payload)
        json_response = json.loads(response.json())
        print("json_response:",json_response)
    except:
        print("Failed user creation request or user")

def check_app_authentication(timenow):
    # print("Trying Authentication")
    # timenow = datetime.now()
    try:
        payload = "{\"email\": \"test@securethebox.us\", \"password\": \"changemestb\"}"
        headers = {'Content-Type': "application/json"}
        response = requests.request("POST", "http://juice-shop-charles.us-west1-a.securethebox.us/rest/user/login", data=payload, headers=headers)
        json_response = json.loads(response.text)
        # print("Response:",json_response['authentication']['umail'])
        if json_response['authentication']['umail'] == "test@securethebox.us":
            # print("Success...",json_response['authentication']['umail'])
            return "success"
            # socketio.emit('api_user_login', {'api_user_login':'success', 'startTime':str(timenow.isoformat()), 'endTime':str((timenow+timedelta(seconds=1)).isoformat()), 'title':'up'})
        else:
            # print("Failed...",json_response['authentication']['umail'])
            return "failed"
            # socketio.emit('api_user_login', {'api_user_login':'failed', 'startTime':str(timenow.isoformat()), 'endTime':str((timenow+timedelta(seconds=1)).isoformat()), 'title':'down'})
    except:
        # print("Failed to authenticate")
        return "failed"
        # socketio.emit('api_user_login', {'api_user_login':'failed', 'startTime':str(timenow.isoformat()), 'endTime':str((timenow+timedelta(seconds=1)).isoformat()), 'title':'down'})

"""
/product/search?
/api/Users
/api/Products
/api/BasketItems
/api/Baskets
/rest/Basket
/api/Complaints
/file-upload
/ftp

"""


@socketio.on_error()
def error_handler(e):
    pass
    # timenow = datetime.now()
    # socketio.emit('my_response', {'app_status':'offline', 'startTime':str(timenow.isoformat()), 'endTime':str(timenow+timedelta(seconds=1)), 'title':'down'})

@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)
    try:
        print("Trying thread again")
    except:
        print("Something happened...")

if __name__ == '__main__':
    socketio.run(app, port=6600, debug=True)
