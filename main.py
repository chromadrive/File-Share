from room import Room
from flask import Flask, request, render_template, redirect
try:
    from urllib.parse import urlparse  # Python 3
except ImportError:
    from urlparse import urlparse  # Python 2 (ugh)

host = 'http://localhost:5000/' # Change for deployment

app = Flask(__name__)

rooms = {}

@app.route('/', methods=['GET'])
def index():
    room_code = "TEST" # for testing, should obviously be changed to random later
    new_room = Room(room_code)
    rooms[room_code] = new_room
    print("Created room " + room_code)
    return redirect(host + "" + room_code + "")

@app.route('/<room_code>') # Reached with <host>/<room_code>
def join_room(room_code):
    print(room_code)
    if room_code in rooms:
        return render_template('room.html')
    else:
        return render_template('404.html')

# Other methods

# Start app
if __name__ == '__main__':
    app.run(debug=True)