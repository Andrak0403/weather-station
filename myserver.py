from flask import Flask, render_template, request, Response, jsonify,make_response
import datetime

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
   now = datetime.datetime.now()
   timeString = now.strftime("%d-%m-%Y %H:%M")
   templateData = {
      'title' : 'Wetherstation grupp 3!',
      'time': timeString,
      }
   return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='192.168.0.39', port=80 , debug=True)
