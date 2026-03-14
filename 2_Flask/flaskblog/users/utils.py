import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):

    #这一步是生成随机文件名防止重名
    random_hex = secrets.token_hex(8)

    #在python中，人们如果为了丢弃变量名会使用下划线作为变量名
    #如果你不使用下划线，那么IDE可能会认为你不使用它
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    #下面几步是网站优化，管理用户导入的图片
    output_size = (125, 125)
    i = Image.open(form_picture)
    #使用thumbnail()方法等比压缩图片，最大尺寸为125x125像素
    i.thumbnail(output_size)
    #这一步是将上传的图片保存到服务器的指定路径
    i.save(picture_path)

    #返回生成的文件名，用于存入数据库
    return picture_fn

def send_reset_email(user):
    #这一步是生成密钥
    token = user.get_reset_token()
    #我们从flask_mail里面导入的Message类可以帮助我们完成发送邮箱
    #sender就是我们的公司邮箱，recipients是我们要发给谁，body就是我们的内容
    #里面的url_for有token和_external参数需要我们手动传入
    msg = Message('Password Reset Request',
              sender=os.environ.get('MAIL_USERNAME'),
              recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    with mail.connect() as conn:
        conn.send(msg)