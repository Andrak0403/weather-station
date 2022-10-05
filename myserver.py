from flask import Flask, render_template, request, Response, jsonify,make_response
from pathlib import Path
import datetime
import time
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
   now = datetime.datetime.now()
   timeString = now.strftime("%d-%m-%Y %H:%M")
   txt = Path('data.txt').read_text()
   data = txt.split(",")
   vind = data[0]
   temp = data[1]
   templateData = {
      'title' : 'Wetherstation grupp 3!',
      'time': timeString,
      'vind':vind, 
      'temp':temp,
      }
   return render_template('index.html', **templateData)

   
if __name__ == "__main__":
   app.run(host='192.168.0.39', port=80 , debug=True)
