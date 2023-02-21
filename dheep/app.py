# from flask import Flask,render_template,request
# import sqlite3 as sql


# app = Flask(__name__)

# @app.route("/")
# def sign_up():
#     if request.form.get("first_name") != None:
#         first_name = request.form.get("first_name")
#         last_name = request.form.get("last_name")
#         email_id = request.form.get("email_id")
#         otp = request.form.get("otp")
#         password = request.form.get("password")
#         confirm_password = request.form.get("confirm_password")
#         x = {"first_name":first_name,"last_name":last_name,"email_id":email_id,"otp":otp,"password":password,"confirm_password":confirm_password}
#         conn = sql.connect("portaldb.db")
#         cur =conn.cursor()
#         cur.execute("insert into sign_up (first_name,last_name,email,otp,password,confirm_password) values (?,?,?,?,?,?)", 
#             (first_name,last_name,email_id,otp,password,confirm_password))
#         conn.commit()   
#     return render_template("index.html", data = x)

# @app.route("/log_in")
# def log_in():
#     if request.form.get("email_id") != None:
#         email_id = request.form.get("email_id")
#         password = request.form.get("password")
#         conn = sql.connect("portaldb.db")
#         cur =conn.cursor()
#         cur.execute("select email_id,password from sign_up")
#         data = cur.fetchall()
#         print(data)
#         for i in data:
#             if i[0] == email_id and i[1] == password:
#                 return render_template("indexpg")
            
#         else:
#             return render_template("log_inpg")
                
       








# if __name__ == "__main__":
#     app.run(debug=True)



import pyotp
import smtplib
from email.mime.text import MIMEText

# Set up the TOTP generator with a secret key
# totp = pyotp.TOTP('23102000')

# Generate the OTP
otp = "DGH654"

# Set up the email message
msg = MIMEText(f'Your OTP is {otp}')
msg['Subject'] = 'Your OTP'
msg['From'] = 'monishachezhain@gmail.com'
msg['To'] = 'sivaranjani650907@gmail.com'

# Send the email using the SMTP server of your email provider
s = smtplib.SMTP('smtp.gmail.com', 587) # replace with your email provider's SMTP server
s.starttls()
s.login('monishachezhain@gmail.com', 'Cse@1822') # replace with your email address and password
s.sendmail('monishachezhain@gmail.com', ['sivaranjani650907@gmail.com'], msg.as_string())
s.quit()