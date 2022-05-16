from flask_login import UserMixin
from requests import session
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
class User(db.Model,UserMixin):
  __tablename__='users'
  id = db.Column(db.Integer,primary_key = True)
  email = db.Column(db.String(255),unique = True,index=True)
  pass_secure = db.Column(db.String(255))
  
  @property
  def password(self):
    raise AttributeError('Encrypted')
  
  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)
    
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)
  
  
class Blog(db.Model,UserMixin):
  __tablename__='blogs'
  id = db.Column(db.Integer,primary_key = True)
  title = db.Column(db.String(30))
  author = db.Column(db.String(25))
  blog_post = db.Column(db.String())
  date_posted = db.Column(db.DateTime,default=datetime.utcnow)
  comments = db.relationship('Comment',backref='blog',lazy='dynamic')

  
  # poster = db.Column(db.LargeBinary)
  
  def save_blog(self):
    db.session.add(self)
    db.session.commit()
    
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    
  @classmethod
  def get_blog(cls, id):
    blogs = Blog.query.filter_by(id=id).all()
    return blogs
  

class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.String(255))
  blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id',ondelete='SET NULL'),nullable = True) 
  blog_pic = db.Column(db.String(255))
  
  def save_comment(self):
    if self not in db.session:
        db.session.add(self)
        db.session.commit()
  def delete(self):
      db.session.remove(self)
      db.session.commit()

        
  @classmethod
  def get_comments(cls,blog_post):
     comments = Comment.query.filter_by(blog_post=blog_post).all()
     return comments
   
  def __repr__(self):
    return f'Comment {self.comment}'
  
class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'
      

    

