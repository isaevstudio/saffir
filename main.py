from flask import Flask,render_template, request, redirect, url_for
import pandas as pd
import smtplib
from forms import ContactUs, Admin
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.utils import secure_filename
import os
from email.mime.base import MIMEBase
from email import encoders
from decouple import config
from flask_wtf.csrf import CSRFProtect


import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST']) 
def home():


    smtp_port = app.config['SMTP_PORT']
    smtp_server = app.config['SMTP_SERVER']
    email_from = app.config['EMAIL_FROM']
    email_list = app.config['EMAIL_LIST']
    pswd = app.config['PSWD']


    form = ContactUs() 

    if request.method == 'POST' and form.validate_on_submit():

            subject = "SAFFIR-ВЕБСАЙТ"
            full_name = form.name.data
            email = form.email.data
            phone = form.phone.data
            comment = form.comment.data

            def send_emails(email_list,full_name,email,phone,comment):

                    body = f"""Name: {full_name}\nEmail: {email}\nPhone: {phone}\n\n{comment}"""

                    msg = MIMEMultipart()
                    msg['From'] = email_from
                    msg['To'] = email_list
                    msg['Subject'] = subject

                    # Attach the body of the message
                    msg.attach(MIMEText(body, 'plain'))
                    
                    # Cast as string
                    text = msg.as_string()

                    # Connect with the server
                    print("Connecting to server...")
                    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
                    TIE_server.starttls()
                    TIE_server.login(email_from, pswd)
                    print("Succesfully connected to server")
                    print()

                    # Send emails to "person" as list is iterated
                    print(f"Sending email to: {email_list}...")
                    TIE_server.sendmail(email_from, email_list, text)
                    print(f"Email sent to: {email_list}")
                    print()

                    # Close the port
                    TIE_server.quit()

            # Run the function
            send_emails(email_list, full_name, email, phone, comment)

            form=ContactUs(formdata=None) 

    news = pd.read_excel(r'./data/news-info.xlsx')
    df_news=[]

    for i in news.values:  
        df_news.append(i[:][1:])



    return render_template('home.html',title='SAFFIR', form=form, df_news=df_news)
    

@app.route('/admin', methods=['GET','POST'])
def login_admin():
    if request.method == 'POST':
        usr = request.form['uname']
        pwd = request.form['psw']

        if (app.config['USR'] == usr) & (app.config['PSW'] == pwd):
            return redirect(url_for('admin'))
        else:
            return render_template('ru/login.html',title='SAFFIR') 
    return render_template('login.html',title='SAFFIR') 

@app.route('/admin-panel', methods=['GET','POST'])
def admin():

    form = Admin() 

    if request.method == 'POST' and form.validate_on_submit():

        myfile = form.fileUploaded_news.data

        if secure_filename(myfile.filename) != '':
            myfile.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['REFRESH_DATA'], secure_filename(myfile.filename)))

        form=Admin(formdata=None) 
    
    return render_template('add_file.html',title='SAFFIR', form=form) 

if __name__ == '__main__':
    # serve(app, host="0.0.0.0", port=8080)
    app.run()