from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'PUll request World!222222'

if __name__ == '__main__':
    app.run()
