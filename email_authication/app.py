import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
#adding TLS security 
server.starttls()
#get your app password of gmail ----as directed in the video
password='hcwa okmk piel xwhc'
server.login('sivaranjanir276@gmail.com',password)
print(server)
#generate OTP using random.randint() function
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(otp)
sender='sivaranjanir276@gmail.com'  #write email id of sender
receiver='rakshitamurali1708@gmail.com' #write email of receiver
#sendi
server.sendmail(sender,receiver,msg)
server.quit()

