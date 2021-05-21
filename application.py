from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/hello')
def hello():
    return 'Hello Hello'

if __name__ == '__main__':
	app.debug = True
	app.run()
		
