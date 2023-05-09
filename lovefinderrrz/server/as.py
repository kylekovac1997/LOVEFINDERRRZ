from datetime import datetime
from flask import Flask, Response, jsonify, request, session, redirect
import psycopg2
import os
import bcrypt
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

app.config["SECRET_KEY"] = 'my_secret_key'


@app.route('/api/login', methods=['POST'])
def login():

    username = request.json.get('username')
    password = request.json.get('password').encode("utf-8")
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"

    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()
    cursor.execute(
        "SELECT password_hash, admin FROM users WHERE username = %(username)s",
        {'username': username})

    user = cursor.fetchone()

    if user:
        password_hash = user[0].encode('utf-8')
        is_admin = user[1]
        if bcrypt.checkpw(password, password_hash):
            session['is_admin'] = is_admin
            session['username'] = username
            return jsonify({'is_admin': is_admin})

    return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/api/admin', methods=['GET'])
def admin():
 
    if session.get('is_admin'):
   
        username = session.get('username')
        os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"

        connect = psycopg2.connect(os.environ["DATABASE_URL"])
        cursor = connect.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            "SELECT username, email, firstname, lastname, userid FROM users WHERE admin = true AND username = %s",
            (username,))
        user = cursor.fetchall()
        return jsonify(user=user)


@app.route('/api/user', methods=['GET'])
def user():
    username = session.get('username')
    if username:
        os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
        connect = psycopg2.connect(os.environ["DATABASE_URL"])
        cursor = connect.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            "SELECT username, email, firstname, lastname, userid FROM users WHERE username = %s",
            (username,))
        user = cursor.fetchall()
        return jsonify(user=user)
    
@app.route('/api/register', methods=['POST'])
def register():
    firstName = request.json.get('first-name')
    lastName = request.json.get('last-name')
    gender = request.json.get("gender")
    dateofbirth = request.json.get("date-of-birth")
    userName = request.json.get("userName")
    email = request.json.get('email')
    phoneNumber = request.json.get('phoneNumber')
    password = request.json.get('Password')
    password_hash = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode('utf-8')
    createdon = datetime.now()
    active = True
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"

    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()
    cursor.execute("""
        INSERT INTO users(firstname, lastname, gender, username, email, mobile, password_hash, createdon, active, dateofbirth)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """, (firstName, lastName, gender, userName, email, phoneNumber, password_hash, createdon, active, dateofbirth))
    connect.commit()
    cursor.close()
    connect.close()
    return jsonify({'message': 'You have made a new account'})

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'You have been logged out'})


if __name__ == '__main__':
    app.run(debug=True)