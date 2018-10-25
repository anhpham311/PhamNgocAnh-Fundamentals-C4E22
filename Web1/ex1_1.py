from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:w>/<int:h>")
def calculate_bmi(w, h):
    bmi = w/h 
    if bmi < 16:
        return "Severely underweight"
    if 16 <= bmi < 18.5:
        return "Underweight"
    if 18.5 <= bmi < 25:
        return "Normal"
    if 25 <= bmi < 30: 
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
  app.run(debug=True)