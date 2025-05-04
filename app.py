from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///signed_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'{self.name}'

with app.app_context():
    db.create_all()
    
@app.route('/')
def home():
    # users = UserData(id = 1, name = 'John Doe', email = '12@yahoo.com', password = '1234')
    # db.session.add(users)
    # db.session.commit()
    # return 'Hello, World!'
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        new_user = UserData(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return render_template('signup.html', success=True)
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
