from flask import render_template,request,redirect,url_for
from flask_login import login_required
from . import main
from ..models import Blog
from ..requests import get_random_quote
from ..models import Blog,Comment
from .forms import CommentsForm

@main.route('/')
def index():
    quote = get_random_quote()
    blog_list = Blog.query.order_by(Blog.date_posted.desc()).all()
    return render_template('index.html',quote=quote,blog_list=blog_list)

@main.route('/readmore')
def readmore():
    # # blog = Blog.query.get(blog_id=id)
    # blog_clicked= Blog.query.filter_by(blog_id=id).all()
    return render_template('readmore.html')

@main.route('/about')
def about():
    return render_template('about.html')
@main.route('/comment/<int:blog_id>', methods= ['GET', 'POST'])

def comment(blog_id):
    form = CommentsForm()
    blog = Blog.query.get(blog_id)
    comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        blog_id = blog_id
        new_comment = Comment(comment=comment, blog_id=blog_id)
        new_comment.save_comment()
        return redirect(url_for('.comment',blog_id=blog_id))
    return render_template('comments.html', form =form, blog = blog,comments=comments)
        