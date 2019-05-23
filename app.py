from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

# create the flask application
app = Flask(__name__)

# /info route returns information about the application
@app.route('/info', methods=['GET'])
@cross_origin()
def info_route():
  return jsonify({
    'app'         : "Bigfoot Classinator Twitter Client",
    'version'     : "1.0.0",
    'attribution' : "AI by DataRobot"
  })

# kick off the flask
if __name__ == '__main__':
  app.run()
