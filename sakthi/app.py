from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient

app=Flask(__name__)

@app.route("/home")
def welCome():
    return "<h1>welcome</h1>"

@app.route("/signup",methods=["POST","GET"])
def signUp():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password1=request.form.get("password1")
        password2=request.form.get("password2")

        client=MongoClient("mongodb://localhost:27017")
        database=client.campusDrive
        collection=database.signUp
        data=collection.find()
        for i in data:
            if i["email"]==email:
                return render_template("signUp.html")
        client.close()

        if password1==password2:
            password=password1

            client=MongoClient("mongodb://localhost:27017")
            database=client.campusDrive
            collection=database.signUp
            collection.insert_one({"username":name,"email":email,"password":password})
            client.close()
        else:
            return render_template("signUp.html")

        return render_template("logIn.html")

    return render_template("signUp.html")

@app.route("/",methods=["POST","GET"])
def logIn():
    if request.method=="POST":
        name_email=request.form.get("name_email")
        password=request.form.get("password")
        client=MongoClient("mongodb://localhost:27017")
        database=client.campusDrive
        collection=database.signUp
        data=collection.find()
        l=[]
        for i in data:
            l.append(i)
        client.close()
        for i in l:
            if (i["email"]==name_email or i["username"]==name_email) and i["password"]==password:
                return render_template("index.html")   
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)