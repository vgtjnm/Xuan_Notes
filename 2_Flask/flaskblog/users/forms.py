from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    #username是变量名,StringField是文本框，就是给人打字的地方，填写信息
    #PasswordField密码框，特殊文本，输入会变成圆点
    #SubmitField提交按钮
    #SF里面的参数第一个是文本框上面的文字，可任意填写
    #第二个参数validators是验证器列表，检查输入是否合规
    #DataRequired是必须输入,Length是限制字符
    #有一些需要注意的小细节
    #第一个参数不只是上面的文字，更准确的理解这是 label（标签）
    #label的作用有用户界面标识，HTML标签关联，错误信息引用，表单对象属性，国际化基础
    #注意拼写DataRequired,不要写错
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#我来解释一下这个更新用户的代码的意思
#我们创建一个更新用户表单的类，类继承自flask_wtf里的FlaskForm
#表单里有两个文本框和一个按钮框
#文本框的参数第一个是名字，第二个是验证器
#验证器里第一个参数是防止输入为空，第二个参数是限制输入字符数
#之后是两个类方法，但是在flask_wtf里他们是自定义验证器
#之所以叫做自定义验证器是因为他是flask_wtf的一个命名约定
#在flask_wtf的源码里，会自动执行以"validate_"开头的所有方法
#但是必须按照命名约定去写，否则就是普通方法
#"validate_"后面的字符要和设定的文本框一致，self后面的参数也要一致

#下面来说一个重要概念，FlaskForm的源码设计是怎么调用自定义验证器的
#当你调用form.validate_on_submit()时，他才会调用
#然后就是自定义验证器的返回值根本不重要，flaskform只在乎ValidationError
#只有抛出异常时才算验证失败，否则正常运行
#另外补充一个python函数知识，要是函数没有返回值，python会返回None

#然后就是"form.validate_on_submit()"和StringField的关系
#validate_on_submit()是方法，SubmitField是数据
#用户点击SubmitField浏览器会发送POST请求，Flask接收请求，之后执行路由
#validate_on_submit()检测到是POST请求，就开始执行所有验证器
#还有个重要概念，点击SubmitField并不会提醒计算机跑验证，但是会发送POST请求
#真正监督计算机跑验证的是validate_on_submit()这个方法
#验证器是由validate_on_submit()主动调用的，不是按钮直接触发的

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        #username是一个输入框，username.data就是用户在里面输入的内容
        #current_user是用户已经登录的账户，这一步是不能让输入的名字和原账户重名
        if username.data != current_user.username:
            #这一步是从数据库里找相同名字，如果没有就是空
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('That is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password')