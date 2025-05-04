from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    dataset= {
            'name': 'John Doe',
            'email': 'jd@john.com'
            }
    return dataset

if __name__ == '__main__':
    app.run(debug=True, port=5000)