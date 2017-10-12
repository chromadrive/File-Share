# FilePost
### A room-based approach to file sharing
![Screenshot](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/545/859/datas/gallery.jpg)

__FilePost__ is a simple no-frills file sharing service built with Python. It takes a room-based approach - much like a chatroom, but for files. You share a room code in the form of an English word with your friends, and once they join you can send and receive files freely from anyone in the room. You can also specify specific people to send a file to, or select no one if you want a file to go to everyone.

This was made by David Xiong ([@chromadrive](https://github.com/chromadrive)), Zeyana Musthafa ([@ZeyanaAM](https://github.com/ZeyanaAM)), and Mesut Yang ([@mesutyang97](https://github.com/mesutyang97)) in 36 hours for CalHacks 2017. Check out the DevPost [here](https://devpost.com/software/filepost), or [try out the demo](http://filepost.herokuapp.com/)!

## Installation
We reccomend using a virtualenv if you're running an instance on your local machine (`sudo apt install virtualenv` if you don't have it already). Then:

```
virtualenv filepost
source filepost/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
Then the website should be live on `localhost:5000` 

## Deployment
Before deploying, make sure to set the `host` variable in `main.py` to whichever hostname you will be occupying. You may also need to change the `port` depending on which platform you are using. 