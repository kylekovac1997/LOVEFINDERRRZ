import base64
from datetime import datetime
from flask import Flask, jsonify, request, session, send_from_directory
import psycopg2
import os
import bcrypt
from flask_caching import Cache
#https://flask-caching.readthedocs.io/en/latest/

from psycopg2.extras import RealDictCursor
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__name__, static_folder='static', static_url_path='/')
app.config["SECRET_KEY"] = 'my_secret_key'
cache.init_app(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)



@app.route('/api/login', methods=['POST'])
@cache.cached(timeout=50)
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

    return jsonify({'message': 'Invalid username or password'})


@app.route('/api/admin', methods=['GET'])
@cache.cached(timeout=50)
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

@app.route('/api/admin/searchUser', methods=['POST'])
@cache.cached(timeout=50)
def adminSearch():
    if request.method == 'POST':
        search_email = request.json.get('search_email', '')
        search_username = request.json.get('search_username', '')
        search_firstname = request.json.get('search_firstname', '')
        search_lastname = request.json.get('search_lastname', '')
        search_gender = request.json.get('search_gender', '')
        search_mobile = request.json.get('search_mobile', '')
        search_dateofbirth = request.json.get('search_dob', '')
        os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"

        connect = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connect.cursor()
        cursor.execute("""
            SELECT * FROM users WHERE
            (userid::text LIKE %s OR %s = '') AND
            (LOWER(email) LIKE LOWER(%s) OR %s = '') AND
            (LOWER(username) LIKE LOWER(%s) OR %s = '') AND
            (LOWER(firstname) LIKE LOWER(%s) OR %s = '') AND
            (LOWER(lastname) LIKE LOWER(%s) OR %s = '') AND
            (LOWER(gender) LIKE LOWER(%s) OR %s = '') AND
            (mobile::text LIKE %s OR %s = '') AND
            (dateofbirth::text LIKE %s OR %s = '')
        """, (f'%{search_username}%', search_username, f'%{search_email}%', search_email, f'%{search_username}%', search_username, f'%{search_firstname}%', search_firstname, f'%{search_lastname}%', search_lastname, f'%{search_gender}%', search_gender, f'%{search_mobile}%', search_mobile, f'%{search_dateofbirth}%', search_dateofbirth))
        results = cursor.fetchall()
        connect.close()
        return jsonify(results=results)




@app.route('/api/user', methods=['GET'])
@cache.cached(timeout=70)
def user():
    username = session.get('username')

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
        user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')

    cursor.close()
    connect.close()

    return jsonify(users=users)

@app.route('/api/home', methods=['GET'])
@cache.cached(timeout=70)
def home():

    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"

    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "SELECT username, profile_picture FROM users LEFT JOIN user_profiles ON users.userid = user_profiles.userid",
    )

    users = cursor.fetchall()

    for user in users:
        profile_picture = user['profile_picture']
        user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')

    cursor.close()
    connect.close()

    return jsonify(users=users)

@app.route('/api/UserProfiles/<username>', methods=['GET'])
@cache.cached(timeout=70)
def userProfiles(username):
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
        user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')

    cursor.close()
    connect.close()

    return jsonify(users=users)


    
@app.route('/api/register', methods=['POST'])
@cache.cached(timeout=50)
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

@app.route('/api/users', methods=['POST'])
@cache.cached(timeout=50)
def userprofile():
    profile_picture = request.files.get('profile_picture').read()

    interests = request.form.get('interests')
    profile_description = request.form.get('profile_description')

    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()
    cursor.execute(
        """INSERT INTO user_profiles (profile_picture, interests, profile_description)
           VALUES (%s, %s, %s)""",
        (profile_picture, interests, profile_description))

    connect.commit()
    cursor.close()
    connect.close()

    return jsonify({'message': 'User profile created'})




@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'You have been logged out'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
