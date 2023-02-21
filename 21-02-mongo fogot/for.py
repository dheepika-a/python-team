from flask import Flask,render_template,request
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://127.0.0.1:27017")

@app.route("/forgotpassword", methods=["POST","GET"])
def forgot():
    client=MongoClient("mongodb://localhost:27017")
    if request.form.get("email")!=None:
       email=request.form.get("email")
       otp=request.form.get("otp")
       password=request.form.get("otp")
       newpassword=request.form.get("otp")
       database=client.details
       collect=database.forgot
       collect.insert_one({
          "email":email,
          "otp":otp,
          "password":password,
          "newpassword":newpassword})
       client.close()
    return render_template("insert.html")