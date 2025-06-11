from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return 'Hello, Flask!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
