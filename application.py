from flask import Flask

application = Flask(__name__)

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

application.add_url_rule('/', 'index', say_hello())

application.add_url_rule('/<username>', 'hello', (lambda username:
   say_hello(username)))

# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()
