import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://127.0.0.1:27017")

#adding TLS security 
server.starttls()
#get your app password of gmail ----as directed in the video
password='hcwa okmk piel xwhc'
server.login('sivaranjanir276@gmail.com',password)
print(server)
#generate OTP using random.randint() function
genotp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(genotp)
print(genotp)
sender='sivaranjanir276@gmail.com'  #write email id of sender
#receiver='rakshitamurali1708@gmail.com' #write email of receiver
#sendi
server.sendmail(sender,receiver,msg)
server.quit()



@app.route("/forgotpassword", methods=["POST","GET"])
def forgot():
    client=MongoClient("mongodb://localhost:27017")
    if request.form.get("email")!=None:
        email=request.form.get("email")
        otp=request.form.get("otp")
        password=request.form.get("password")
        newpassword=request.form.get("newpassword")
        database=client.details
        collect=database.forgot
        collect.insert_one({
            "email":email,
            "password":password,
            "newpassword":newpassword
            })
        client.close()
    if(genotp==otp):
        return redirect(url_for)
    return render_template("insert.html")


