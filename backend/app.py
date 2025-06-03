# Flask app placeholder
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'CogniShield Backend Running'

if __name__ == '__main__':
    app.run(debug=True)
