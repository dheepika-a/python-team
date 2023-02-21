from flask import Flask,render_template,request,redirect,url_for,flash,get_flashed_messages,session,jsonify
from pymongo import MongoClient

app=Flask("__name__")
app.secret_key="sakthi25"

@app.route("/Signup",methods=["POST","GET"])
def Signup():
    if request.method=="POST":
        id= request.form.get("id")
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
       
        client=MongoClient("mongodb://127.0.0.1:27017")
        database=client.users_list
        collection=database.session_detail
        data=collection.find()
        l=[]
        for i in data:
            l.append(i)
            print(i)
        print(l)
        client.close()
        for i in l:
            if i["id"]==id or i["email"]== email:
                return "User already exist please enter a valid Email ID "
            

        client=MongoClient("mongodb://127.0.0.1:27017")
        database=client.users_list
        collection=database.session_detail
        collection.insert_one({"id":id,"username":username,"email":email,"password":password})
        client.close()
        
        return "successfully registred"
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)