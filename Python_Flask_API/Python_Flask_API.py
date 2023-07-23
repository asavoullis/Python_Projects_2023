from flask import Flask, request, jsonify

# JSON = JavaScript Object Notation
# It is a collection of key value pairs like a python dictionary

# create our flask application
app = Flask(__name__)

# we then need to create a root
# a root is essentially an endpoint - a location on our API
# that we can go to, to get some kind of data
# there are different types of roots


# to make this accessible what we need to do is to add a decorator
# we then put in brackets the path that we are going to access, in this case / which will be the default root
# the root is really what comes after the slash in the URL address bar
@app.route("/")
def home():
    """
    Inside this function we want the user to have access to when they reach this root
    """
    return "Home"




# HTML methods
# GET, POST, PUT, DELETE
# GET - request data from a specified server (retrieve some value from the server)
# POST - Create a resource
# PUT - Update a resource (Alter or modify existing data)
# DELETE - Delete a resource - (Delete or Remove data from a database or resource that we are accessing)



# a path parameter is a dynamic value that you can pass in the path of a URL that we'll be able to access inside of our route
# in this case <user_id>
@app.route("/get-user/<user_id>")
def get_user(user_id):

    # in flask we create a dictionary 
    user_data = {
        "user_id": user_id,
        "name": "Andrew Doe",
        "email": "andrew.doe@example.com"
    }

    # whenever we are accessing a root, we have the ability to pass something known as a query parameter
    # which is essentially an extra value that is included after the main path "get-user/123?extra=hello world"
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    # we then jsonify that dictionary and that's what we can return to the user
    # this allows flask to actually parse this value and return as JSON data and a status code
    # 200 is the default status code of success but you can pass other HTTP status codes as well
    return jsonify(user_data), 200



if __name__ == '__main__':
    # this will run our flask server
    app.run(debug=True)