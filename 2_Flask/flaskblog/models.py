from datetime import datetime
from itsdangerous import URLSafeTimedSerializer
from flaskblog import db, login_manager
from flask import current_app
from flask_login import UserMixin

#这里corey讲了为啥在user报错而不是db
#我们先运行了flaskblog,然后执行了从models导入User和Post
#python从一个模块导入任何东西，他仍然会运行整个模块
#当python运行models时，它会进入我们的模型脚本，然后尝试执行导入操作，就是from flask import db那一步
#corey原本以为在这一步会失败，因为我们已经见过flaskblog了，它就是我们刚才经过的地方
#所以他以为程序会说，嘿我们已经见过flaskblog了但是并没有db变量
#但是程序却是在用户导入时报错了，这是为何？
#因为我们运行flaskblog时直接使用python，python直接调用脚本时会将脚本命名为"__main__"
#所以当我们运行到from flaskblog import db时，python实际上还没见过flaskblog，所以它会回到flaskblog
#flaskblog运行from models import User, Post时，因为我们已经运行过models了，但是并没有找到User和Post
#所以报错点在User而不是db
#想让报错点出现在db，直接把flaskblog改为"__main__"就行了
#当然想要不报错，最终解决方案是把flaskblog的models导入延后

@login_manager.user_loader
def load_user(user_id):
    #使用get方法可以得到用户的信息
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    #用户需要重置他的密码，但是我们需要他证明“他是他”，不能随便改
    #我们的做法是给用户邮箱发一个带特殊链接的邮箱，链接有一个令牌，只有拿到这个令牌的人才能重置密码
    #所以下面这两个方法的作用就是生成和验证令牌

    #expires_in参数用来设置令牌的有效期，单位是秒，我们这里默认3600，开发者也可以手动设置
    def get_reset_token(self, expires_in=3600):


        #这一步Serializer的第二个参数expires_in就是官方支持的过期时间
        #它会在生成 token 时 自动写入时间戳
        #在 loads() 时 自动校验是否过期
        #过期直接抛异常（SignatureExpired）
        #还有一件很重要的事，为了防止循环导入的折腾，我们直接用current_app代替app,防止app为空
        #还有一件事因为itsdangerous的版本问题导致我们不能使用Serializer，而是使用URLSafeTimedSerializer代替
        #expires_in这个参数我们没有用，只是放在这里告诉你使用的有效期，新版itsdangerous过期时间在验证时设置

        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

        #下面聊一下dumps的作用
        #他在内部做了这几件事：
        #序列化（serialize），加签名（sign），记录时间，编码成字符串
        #简单理解为dumps = 序列化 + 签名（防篡改）+ 编码
        #dumps对应的反操作角loads，作用是：
        #解码，验证签名，检查是否过期，还原成原来的 Python 数据

        return s.dumps({'user_id': self.id})


    #@staticmethod表示这个方法不依赖某个具体 User 实例
    @staticmethod
    def verify_reset_token(token, expires_in=3600):

        #这行的作用是创建反序列化器
        #用和 dumps 时 同一个 SECRET_KEY，否则验证一定失败

        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

        #下面来聊一下核心代码loads
        #loads会做四件事
        #验证 token 是否被篡改，验证签名是否正确，验证是否过期，反序列化，拿回原始数据
        #任何一步失败，说明token可能被改过，过期，乱传，它会直接抛出异常

        #user_id = data['user_id']中，data就是我们前面dumps的字典
        #except意思就是异常处理，如果try中抛出异常就会执行except的代码，我们一般是返回None
        #User.query.get(user_id)会根据user_id查数据库

        try:
            #这种写法是语法糖
            #等效的原版是：
            #data = s.loads(token, max_age=expires_in)
            #user_id = data['user_id']
            user_id = s.loads(token, max_age=expires_in)['user_id']
        except:
            return None
        return User.query.get(user_id)

    #还记得吗？repr方法是打印自己时控制返回值
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"