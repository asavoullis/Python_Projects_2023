from flask import Flask
from flask_restful import Api, Resource

# Create a Flask web application instance (app)
app = Flask(__name__)
# Create an instance of the Api class, which is provided by Flask-RESTful
# wrap our app in an API - restful api
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}
    
    def post(self):
        return {"data": "Posted"}

db = {
    "tom": {"age": 19, "gender": "male"},
    "bill": {"age": 50, "gender": "male"},
    "jessica": {"age": 33, "gender": "female"},
    "daniela": {"age": 23, "gender": "female"},
         }

class HelloWorldParam(Resource):
    def get(self, name):
        return db[name]
    
    def post(self):
        return {"data": "Posted"}


api.add_resource(HelloWorld, "/helloworld")
api.add_resource(HelloWorldParam, "/helloworld/<string:name>")

if __name__ == '__main__':
    # start our server - flask app
    # debug = True for development environments - testing
    app.run(debug=True)

