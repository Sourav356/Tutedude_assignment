from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
#changed my actual uri for security reasons
MONGO_URI = "mongodb+srv://souravpuser:pQ7@cluster0.uv4nodo.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["form_db"]
collection = db["form_data"]


# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Form Route
@app.route("/form", methods=["GET", "POST"])
def form():
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            # Insert into MongoDB
            collection.insert_one({
                "name": name,
                "email": email
            })

            return redirect(url_for("success"))

        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)

# Success Route
@app.route("/success")
def success():
    return render_template("success.html")


# Run App
if __name__ == "__main__":
    app.run(debug=True)