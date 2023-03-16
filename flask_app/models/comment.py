from flask_app.config.connection import connectToMySQL
from flask_app.models import post


class Comment:
    DB = "dojo_wall_db"
    def __init__(self, data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_name = None
        
    
    # CRUD METHODS
    
    #CREATE
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO comments
                ( post_id, user_id, content , created_at, updated_at ) 
                VALUES 
                ( %(post_id)s, %(user_id)s, %(content)s , NOW() , NOW() )
                ;"""
        return connectToMySQL(cls.DB).query_db( query, data )
    
    #READ 
    @classmethod
    def get_all(cls):
        query = """SELECT * 
                FROM comments
                ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        
        comments = []
        for row in results:
            comments.append(cls(row))
        return comments
    
    #READ ALL COMMENTS BY POST ID  WITH USERS NAME - 
    @classmethod
    def get_comments_with_user_name(cls):
        query = """SELECT *
                FROM users
                JOIN comments ON users.id = comments.user_id
                JOIN posts ON posts.id = comments.post_id;
                ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        comments = []
        for row in results:
            comment = cls(row)
            user_data = {
                'id': row["users.id"],
                'first_name': row["first_name"],
                'last_name': row["last_name"],
                'email': row["email"],
                'password': '',
                'created_at' : row["created_at"],
                'updated_at' : row["updated_at"],
            }
            comment.user_name = post.Post(user_data)
            comments.append(comment)
        return comments
        
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