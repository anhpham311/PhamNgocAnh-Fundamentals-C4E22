from flask import Flask, render_template
app = Flask(__name__)

@app.route("/bmi/<int:w>/<int:h>")
def calculate_bmi(w, h):
    bmi = w/h 
    if bmi < 16:
        return render_template("su.html")
    if 16 <= bmi < 18.5:
        return render_template("under.html")
    if 18.5 <= bmi < 25:
        return render_template("normal.html")
    if 25 <= bmi < 30: 
        return render_template("overweight.html")
    else:
        return render_template("obese.html")

if __name__ == '__main__':
  app.run(debug=True)