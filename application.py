from flask import Flask, render_template, redirect, request
import os
import pywhatkit as py
app = Flask(__name__)
phone_number = ""
message = ""
time_min ='' 
time_hour =''

@app.route('/', methods=['GET',"POST"])

def home():
    if request.method == "POST":
        phone_number = str(request.form.get('phone_number'))
        message = str(request.form.get('message'))
        time_min = int(request.form.get('time_min'))
        time_hour = int(request.form.get('time_hour'))
        py.sendwhatmsg(phone_number,message,time_hour, time_min)
        return render_template('result.html', add=message)
    return render_template('index.html')


if __name__ == "__main__":
    app.debug=True
    app.run()