from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store (replace with a database in a real application)
users_data = {}

@app.route("/")
def home():
    """Homepage"""
    return "Home"

@app.route("/get-user/<int:user_id>")
def get_user(user_id):
    """Get user data by ID"""
    user_data = users_data.get(user_id)
    if user_data:
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/create-user", methods=["POST"])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        # Validate required fields
        if "user_id" not in data or "name" not in data or "email" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        # Save user data
        user_id = data["user_id"]
        users_data[user_id] = {
            "user_id": user_id,
            "name": data["name"],
            "email": data["email"]
        }
        return jsonify(users_data[user_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/update-user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update user data by ID"""
    try:
        data = request.get_json()
        if user_id not in users_data:
            return jsonify({"error": "User not found"}), 404

        # Update user data
        users_data[user_id].update(data)
        return jsonify(users_data[user_id]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/delete-user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete user data by ID"""
    if user_id in users_data:
        del users_data[user_id]
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
