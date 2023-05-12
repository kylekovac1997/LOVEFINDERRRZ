import psycopg2
from psycopg2.extras import RealDictCursor
import os
import base64
from datetime import datetime
import bcrypt

def get_active_users():
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "SELECT username, profile_picture FROM users LEFT JOIN user_profiles ON users.userid = user_profiles.userid WHERE users.active = true",
    )

    users = cursor.fetchall()

    for user in users:
        profile_picture = user['profile_picture']
        if profile_picture is not None:  
            user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')
        else:
            user['profile_picture'] = ""

    cursor.close()
    connect.close()

    return users


def get_user_profile(username):
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "SELECT * FROM users LEFT JOIN user_profiles ON users.userid = user_profiles.userid WHERE users.username = %s",
        (username,)
    )

    users = cursor.fetchall()

    for user in users:
        profile_picture = user['profile_picture']
        if profile_picture is not None:  
            user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')
        else:
            user['profile_picture'] = ""

    cursor.close()
    connect.close()

    return users

def register_user(user_data):
    firstName = user_data.get('first-name')
    lastName = user_data.get('last-name')
    gender = user_data.get('gender')
    dateofbirth = user_data.get('date-of-birth')
    userName = user_data.get('userName')
    email = user_data.get('email')
    phoneNumber = user_data.get('phoneNumber')
    password = user_data.get('Password')
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
    createdon = datetime.now()
    active = True

    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()

    cursor.execute("""
        INSERT INTO users(firstname, lastname, gender, username, email, mobile, password_hash, createdon, active, dateofbirth)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (firstName, lastName, gender, userName, email, phoneNumber, password_hash, createdon, active, dateofbirth))

    connect.commit()
    cursor.close()
    connect.close()

    return {"message": "Successful"}

def create_user_profile(profile_picture, interests, profile_description):
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()

    cursor.execute(
        """INSERT INTO user_profiles (profile_picture, interests, profile_description)
           VALUES (%s, %s, %s)""",
        (profile_picture, interests, profile_description)
    )

    connect.commit()
    cursor.close()
    connect.close()

    return {"message": "Successful"}