from flask import Flask, request, jsonify
from flask_cors import CORS  # NEW

app = Flask(__name__)
CORS(app)  # NEW: This enables the frontend to talk to the backend

products = {
    "shoes": ["Running Shoes", "Sports Shoes", "Sneakers"],
    "laptop": ["Laptop Bag", "Cooling Pad", "Mouse"],
    "phone": ["Phone Cover", "Screen Guard", "Charger"]
}

@app.get("/recommend")
def recommend():
    item = request.args.get("item", "").lower()
    return jsonify({
        "input": item,
        "recommendations": products.get(item, ["No recommendations available"])
    })

@app.get("/")
def home():
    return "Backend is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
