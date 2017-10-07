from flask import Flask, request, render_template, redirect
try:
    from urllib.parse import urlparse  # Python 3
except ImportError:
    from urlparse import urlparse  # Python 2 (ugh)

host = 'http://localhost:5000/' # Change for deployment

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # create_room()
    # redirect_to_room()

@app.route('/<room_code>') # Reached with <host>/<room_code>
def redirect_short_url(room_code):
    # do_some_stuff_if_room_exists()
    # 404_if_room_doesnt_exist

# Other methods

# Start app
if __name__ == '__main__':
    app.run(debug=True)