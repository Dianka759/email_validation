from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid, Please provide an email address!")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT into emails (email) VALUES (%(email)s);"
        return connectToMySQL('email').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        return  connectToMySQL('email').query_db(query)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM emails WHERE email=%(email)s"
        email_db = connectToMySQL("email").query_db(query,data)
        if len(email_db) < 1:
            return False
        return cls(email_db[0])

    @classmethod
    def delete_email(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL("email").query_db(query,data)