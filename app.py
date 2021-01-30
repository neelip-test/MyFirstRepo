from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return 'Web App with Python Flask!'

# If planning to run thru the terminal
# app.run(host='0.0.0.0', port=81)