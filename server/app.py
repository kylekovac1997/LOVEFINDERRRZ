from flask import Flask, jsonify, request, session
import psycopg2
import os
import bcrypt
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = 'my_secret_key'


@app.route('/api/login', methods=['POST'])
def login():
    # Get user input from request body
    identifier = request.json.get('identifier')
    password = request.json.get('password').encode("utf-8")
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    # Query database for user with given email or username
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()
    cursor.execute(
        "SELECT  userid, email, username, password_hash, admin FROM users WHERE (email=%s OR username=%s)",
        (identifier, identifier))

    user = cursor.fetchone()
    connect.close()
    hashed_password = user[3].encode('utf-8')
    # Check if user exists and password matches
    if user and bcrypt.checkpw(password, hashed_password):
        session['user'] = user[0]
        # Return success message and user data
        response = {
            'message': 'Login successful',
            'user': {
                'email': user[1],
                'username': user[2],
                'admin': user[4]
            }
        }
        return jsonify(response), 200
    else:
        response = {
            'message': 'Invalid email or password'
        }
        return jsonify(response), 401


@app.route('/api/userinfo', methods=['GET'])
def userinfo():
    # Get user ID from session
    user_id = session.get('user')

    # If user is logged in, query database for user info
    if user_id:
        # Query database for user with given ID
        os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
        connect = psycopg2.connect(os.environ["DATABASE_URL"])
        cursor = connect.cursor()
        cursor.execute(
            "SELECT email, username FROM users WHERE userid=%s",
            (user_id,))

        user = cursor.fetchone()
        connect.close()

        # If user is found, return user info
        if user:
            response = {
                'user': {
                    'email': user[0],
                    'username': user[1]
                }
            }
            return jsonify(response), 200
        else:
            # If user is not found, return error message
            response = {
                'message': 'User not found'
            }
            return jsonify(response), 404
    else:
        # If user is not logged in, return error message
        response = {
            'message': 'User not found'
        }
        return jsonify(response), 404


if __name__ == '__main__':
    app.run(debug=True)
