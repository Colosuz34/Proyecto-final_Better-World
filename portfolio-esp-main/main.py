# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    feedback_text = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Feedback {self.name}>'

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<projects>')
def proyecto():
    return render_template('projects.html')

@app.route('/feedback', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        commentary = request.form['text']

        new_feedback = Feedback(name = email, feedback_text = commentary)
        db.session.add(new_feedback)
        db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
