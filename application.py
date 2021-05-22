
from flask import Flask

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda:
    say_hello()))

application.add_url_rule('/<username>', 'hello', (lambda username:
    say_hello(username)))

if __name__ == "__main__":
    application.debug = True
    application.run()
