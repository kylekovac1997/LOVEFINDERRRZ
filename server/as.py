import base64
from datetime import datetime
from flask import Flask, jsonify, request, session, send_from_directory
import psycopg2
import os
import bcrypt
from flask_caching import Cache
from psycopg2.extras import RealDictCursor
#https://flask-caching.readthedocs.io/en/latest/


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

    return jsonify({"message": "Successful"})


@app.route('/api/admin', methods=['GET'])
@cache.cached(timeout=50)
def admin():
        username = session.get('username')
        os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"

        connect = psycopg2.connect(os.environ["DATABASE_URL"])
        cursor = connect.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
        "SELECT * FROM users LEFT JOIN user_profiles ON users.userid = user_profiles.userid WHERE users.username  = %s ",
        (username,)
    )

        admin = cursor.fetchall()

        for user in admin:
            profile_picture = user['profile_picture']
            if profile_picture is not None: 
                user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')
            else:
                user['profile_picture'] = ""
        return jsonify(admin=admin)

@app.route('/api/admin/searchUser', methods=['POST'])
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
        if profile_picture is not None:  
            user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')
        else:
            user['profile_picture'] = ""
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
        "SELECT username, profile_picture FROM users LEFT JOIN user_profiles ON users.userid = user_profiles.userid WHERE users.active = true ",
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

    return jsonify(users=users)

@app.route('/api/UserProfiles/<username>', methods=['GET'])
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
        if profile_picture is not None:  
            user['profile_picture'] = base64.b64encode(profile_picture).decode('utf-8')
        else:
            user['profile_picture'] = ""

    cursor.close()
    connect.close()

    return jsonify(users=users)

@app.route("/api/liked/<int:userid>", methods=["POST"])
def like(userid):
    database_url = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"

    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO user_profiles (liked) VALUES (%s)", (userid,))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({"message": "Successful"})
    
    
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
    return jsonify({"message": "Successful"})

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

    return jsonify({"message": "Successful"})

@app.route('/api/deactivate', methods=['POST'])
def deactivate():
    username = session.get('username')

    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()

    cursor.execute("UPDATE users SET active = false WHERE username = %s", (username,))
    connect.commit()

    cursor.close()
    connect.close()

    return jsonify({"message": "User deactivated"})

@app.route('/api/reactivate', methods=['POST'])
def reactivate():
    username = session.get('username')

    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()

    cursor.execute("UPDATE users SET active = true WHERE username = %s", (username,))
    connect.commit()

    cursor.close()
    connect.close()

    return jsonify({"message": "User reactivated"})

@app.route('/api/sendMessage', methods=["POST"])
def sendMessage():

    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    sender_id = request.json.get('sender_id')
    recipient_id = request.json.get('recipient_id')
    content = request.json.get('content')

    cursor = connect.cursor()
    cursor.execute("INSERT INTO messages (sender_id, recipient_id, content) VALUES (%s, %s, %s)",
                   (sender_id, recipient_id, content))
    connect.commit()
    cursor.close()

    return jsonify({"message": "Message sent successfully"})


@app.route('/api/messages', methods=['GET'])
def get_messages():
    username = session.get('username')

    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor()
    cursor.execute("SELECT userid FROM users WHERE username = %s", (username,))
    user_id = cursor.fetchone()

    if user_id is None:
        return jsonify({"error": "User not found"})

    user_id = user_id[0]
    cursor.close()

    cursor = connect.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT messenger.content, messenger.sender_id, messenger.recipient_id,
               sender.username AS sender_username, recipient.username AS recipient_username
        FROM messages AS messenger
        JOIN users AS sender ON messenger.sender_id = sender.userid
        JOIN users AS recipient ON messenger.recipient_id = recipient.userid
        WHERE messenger.sender_id = %s OR messenger.recipient_id = %s
        ORDER BY messenger.sent_date DESC
    """, (user_id, user_id))
    messages = cursor.fetchall()
    cursor.close()

    return jsonify({"messages": messages})


@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('is_admin', None)
    session.pop('username', None)
    session.clear()
    session.modified = True
    return jsonify({"message": "Successful"})






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
