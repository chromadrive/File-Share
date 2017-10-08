import util
import os
from room import Room
from client import Client
from flask import Flask, request, render_template, redirect, send_from_directory
from flask_socketio import SocketIO, emit, send, join_room, leave_room, rooms
from werkzeug.utils import secure_filename
try:
    from urllib.parse import urlparse  # Python 3
except ImportError:
    from urlparse import urlparse  # Python 2 (ugh)

ON_HEROKU = os.environ.get('ON_HEROKU') # Checks for heroku connection

#host = 'http://localhost:5000/' # Change for deployment
host = 'http://filepost.herokuapp.com/'

app = Flask(__name__)
##
UPLOAD_FOLDER = ''
app.config['SECRET_KEY'] = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
socketio = SocketIO(app)
#

rooms = {}


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
            which = request.form['submit']
            print(which)
            if which == 'New Room':
                #if (groupname == ""):
                room_code = str(util.generate_room_code()) # for testing, should obviously be changed to random later
            #while room_code.upper() in rooms:
            #    room_code = str(util.generate_room_code())
                room_code = room_code.upper()
                new_room = Room(room_code)
                rooms[room_code] = new_room
                print("Created room " + room_code)
                print("User info======" + util.get_user_id())
                return redirect(host + "" + room_code + "")
            elif which == 'Join Room':
                result = request.form
                print(result)
                groupname = result['file']
                print(groupname)
                groupname = groupname.upper()
                if groupname in rooms:
                    return redirect(host + "" + groupname + "")
                else:
                    return render_template('index.html', no_group = "True")

        return render_template('index.html', no_group = "")

@app.route('/<room_code>', methods=['GET', 'POST']) # Reached with <host>/<room_code>
def join_room(room_code):
    room_code = str(room_code.upper()) #.decode("utf-8")
    if room_code in rooms:
        room = rooms[room_code]
        user_id = str(util.get_user_id())
        if user_id not in room.users:
            room.addUser(user_id)
            print(room.users)
        print(room_code)
        print(rooms)
        if request.method == 'POST':
            uploadedFile = request.files['file']
            filename = uploadedFile.filename
            name = room_code + "_" + filename
            print(name)
            uploadedFile.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(name)))
            room.addFile(filename, user_id)
            receivers = ['537.36']
            room.sendTo(filename, receivers)
            print(room.fileSend)
            #print(tempfile.gettempdir())
            return render_template('room.html', room = room, user_id = user_id)

    #if request.method == 'GET':
    	#print('getting')
        #if 'submit' in request.form:
        	#fileget = request.form['submit']
        	#return redirect(host + "" + room_code + "/" + fileget)
    if room_code in rooms:
        room = rooms[room_code]
        user_id = util.get_user_id()
        return render_template('room.html', room = room, user_id = user_id)
    else:
        return render_template('404.html')


@app.route('/files/<room_code>_<filename>', methods=['GET', 'POST'])
def download(room_code, filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    path = room_code + "_" + filename
    print('yoyoyoyos/files/' + path)
    print('uploads' + uploads)
    return send_from_directory(directory=uploads, filename= path)




# Other methods
@socketio.on('my event')
def test_message(message):
    print('hello')
    emit('my response', {'data': 'got it!'})

@socketio.on('message')
def handle_message(message):
    send(message)

"""
@socketio.on('join')
def on_join(data):
    for room in rooms:
        username = data['username']
        if data['room_code'] == room.room_code:
            join_room(room)
            send(username + 'has entered the room.', room=room)
"""
# Start app
if __name__ == '__main__':
    if ON_HEROKU:
        # get the heroku port
        port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
        socketio.run(app, host = host, port = port, debug=True)   
    else:
        socketio.run(app, host = '127.0.0.1', port = 5000)
    #app.run(debug=True)