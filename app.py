from flask import Flask, request
from flask_restful import Api
import database_handler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/insert_link", methods =["POST"])
@cross_origin()
def insert_link():
    link = request.json.get('link')
    date = request.json.get('date')
    device = request.json.get('device')
        
    database_handler.insert_link(link, date, device)
    response = {
        "status": "success"
    }
    return response
@app.route("/get_links", methods= ["GET"])
@cross_origin()
def get_links():
    response = {
        "links" : database_handler.get_all_links()
    }
    return response




if __name__ == '__main__':
    app.run(debug=True)