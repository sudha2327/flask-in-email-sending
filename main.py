from flask import *
from flask_mail import Message,Mail

app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='suganyav459@gmail.com'
app.config['MAIL_PASSWORD']='9597300361'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/')

def index():

    msg=Message('HEY SUDHAGAR',sender='suganyav459@gmail.com',recipients=['sudhagarsvs2332@gmail.com'])
    msg.body='hii broo , how are youu!! enada pannura ????'
    print("sending process")
    mail.send(msg)
    print("mail.send() process")
    return "mail sent  to the   alter recipients pls check" 


if __name__=="__main__":
    app.run(debug=True)
    