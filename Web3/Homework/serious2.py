from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/newbike", methods=["GET","POST"])
def newbike():
    if request.method == "GET":
        return render_template("serious1.html")
    elif request.method == "POST":
        form = request.form
        print(form)
        return "Thank you for your response"

if __name__ == '__main__':
  app.run(debug=True)