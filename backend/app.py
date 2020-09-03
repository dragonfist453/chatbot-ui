from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET','POST'])
def base():
    # Edit this function with chatbot interface
    input_str = (request.get_data().decode('utf-8'))[::-1]  # Reverse string and send just to check if it gets data from server
    return input_str

if __name__=='__main__':
    app.run(host='localhost',port='5000')