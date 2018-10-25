from flask import Flask
app = Flask(__name__)

Users = {
    "annie": {
        "name": "Pham Ngoc Anh",
        "age": 23, 
    },
    "huy": {
        "name": "Nguyen Quang Huy",
        "age": 29
    },
    "tuananh":{
        "name": "Huynh Tuan Anh",
        "age": 20,
    },
}

@app.route("/user/<username>")
def username(username):
    if username in Users:
        return str(Users[username])
    else:
        return "User not found"

if __name__ == "__main__": #set up server
    app.run(debug=True)