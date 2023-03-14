from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import post
from flask_app.models import user


@app.route('/create/post', methods=['POST'])
def create_post():
    user_in_db = user.User.get_by_email(request.form['first_name'])
    session['first_name'] = user_in_db.first_name
    print(session['first_name'])
    post.Post.save(request.form)
        
    return redirect('/dashboard')