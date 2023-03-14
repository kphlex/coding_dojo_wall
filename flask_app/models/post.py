from flask_app.config.connection import connectToMySQL
from flask_app.models import user
from flask import session

class Post:
    DB = "dojo_wall_db"
    def __init__(self, data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_name = None
        
    
    # CRUD METHODS
    
    #CREATE
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO posts 
                ( user_id, content , created_at, updated_at ) 
                VALUES 
                ( %(user_id)s, %(content)s , NOW() , NOW() )
                ;"""
        return connectToMySQL(cls.DB).query_db( query, data )
    
    #READ 
    @classmethod
    def get_all(cls):
        query = """SELECT * 
                FROM posts
                ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        
        posts = []
        for row in results:
            posts.append(cls(row))
        return posts
    
    #READ ALL POSTS WITH USERS NAME - 
    @classmethod
    def get_posts_with_user_name(cls):
        query = """SELECT * 
                FROM posts
                LEFT JOIN users
                ON posts.user_id = user.id
                ;"""
        results = connectToMySQL(cls.DB).query_db( query)
        posts = []
        for row in results:
            post = cls(row)
            user_data = {
                'id': row["user.id"],
                'first_name': row["first_name"],
                'last_name': row["last_name"],
                'email': row["email"],
                'password': row["password"],
                'created_at' : row["posts.created_at"],
                'updated_at' : row["posts.updated_at"],
            }
            post.user_name = user.User(user_data)
            posts.append(post)
        return posts
        
    #READ ONE POST
    @classmethod 
    def get_one(cls, data):
        query = """SELECT * 
                FROM posts 
                WHERE id = %(id)s
                ;"""
        results = connectToMySQL(cls.DB).query_db( query, data)
        return cls(results[0])
    
    #UPDATE
    @classmethod
    def update(cls, data):
        query = """
                UPDATE posts 
                SET content = %(content)s, updated_at = NOW() 
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        
        return results
    
    #DELETE
    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM posts
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results