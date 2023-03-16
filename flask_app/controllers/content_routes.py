from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import post
from flask_app.models import user
from flask_app.models import comment


@app.route('/create/post', methods=['POST'])
def create_post():
    
    print(session['first_name'])
    post.Post.save(request.form)
        
    return redirect('/dashboard')

@app.route('/create/comment', methods=['POST'])
def create_comment():
    comment.Comment.save(request.form)
    return redirect('/dashboard')




@app.route('/edit/post')
def edit_post():
    pass