from flask_wtf import FlaskForm  
from wtforms import TextAreaField, SubmitField, StringField, FileField 
from wtforms.validators import DataRequired, Length, Email



class ContactUs(FlaskForm):  
    name = StringField(validators=[DataRequired(),Length(min=3,max=30)],render_kw={"placeholder": "Имя"})     
    phone = StringField(validators=[DataRequired(),Length(min=3,max=50)],render_kw={"placeholder": "Тел."})     
    email = StringField(validators=[DataRequired(),Email(message=('Acceptable format: example@gmail.com'))],render_kw={"placeholder": "Е-mail: example@gmail.com"}) 
    comment = TextAreaField(render_kw={"placeholder": "Сообщение"})
    submit = SubmitField("Отправить")  



class Admin(FlaskForm):  
    fileUploaded_news = FileField('Upload a file')
    submit = SubmitField("Submit") 