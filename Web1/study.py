from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def about_me():
    return render_template("about_me.html")

@app.route("/school")
def school():
    return redirect("https://techkids.vn/khoa-hoc-lap-trinh/code-for-everyone")

if __name__ == "__main__": #set up server
    app.run(debug=True)