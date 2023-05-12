import base64
from datetime import datetime
from flask import Flask, jsonify, request, session, send_from_directory
import psycopg2
import os
import bcrypt
from flask_caching import Cache
from psycopg2.extras import RealDictCursor
from model.userprofile import get_admin, get_user, search_users
from model.status import deactivate_user, reactivate_user
from model.messages import get_messages, send_message
from model.pages import get_active_users, get_user_profile, register_user, create_user_profile

#https://flask-caching.readthedocs.io/en/latest/


cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__name__, static_folder='static', static_url_path='/')
app.config["SECRET_KEY"] = 'my_secret_key'
cache.init_app(app)

@app.route('/')
def index():
    title = '❤️LOVEFINDERRRZ'
    return send_from_directory(app.static_folder, 'index.html', title=title)

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

    return jsonify({"message": "Successful"})


@app.route('/api/admin', methods=['GET'])
def get_admin_route():
    username = session.get('username')
    admin = get_admin(username)
    return jsonify({"admin": admin})

@app.route('/api/searchusers', methods=['POST'])
def search_users_route():
    search_email = request.json.get('search_email', '')
    search_username = request.json.get('search_username', '')
    search_firstname = request.json.get('search_firstname', '')
    search_lastname = request.json.get('search_lastname', '')
    search_gender = request.json.get('search_gender', '')
    search_mobile = request.json.get('search_mobile', '')
    search_dateofbirth = request.json.get('search_dob', '')
    results = search_users(
        search_email,
        search_username,
        search_firstname,
        search_lastname,
        search_gender,
        search_mobile,
        search_dateofbirth
    )
    return jsonify(results=results)




@app.route('/api/user', methods=['GET'])
def get_user_route():
    username = session.get('username')
    user = get_user(username)
    return jsonify({"user": user})

@app.route('/api/home', methods=['GET'])
@cache.cached(timeout=70)
def home_route():
    users = get_active_users()
    return jsonify(users=users)

@app.route('/api/UserProfiles/<username>', methods=['GET'])
@cache.cached(timeout=70)
def user_profiles(username):
    users = get_user_profile(username)
    return jsonify(users=users)

    
@app.route('/api/register', methods=['POST'])
@cache.cached(timeout=50)
def register():
    user_data = request.json
    result = register_user(user_data)
    return jsonify(result)

@app.route('/api/users', methods=['POST'])
@cache.cached(timeout=50)
def userprofile():
    profile_picture = request.files.get('profile_picture').read()
    interests = request.form.get('interests')
    profile_description = request.form.get('profile_description')

    result = create_user_profile(profile_picture, interests, profile_description)
    return jsonify(result)

@app.route('/api/deactivate', methods=['POST'])
def deactivate():
    username = session.get('username')

    result = deactivate_user(username)
    return jsonify(result)

@app.route('/api/reactivate', methods=['POST'])
def reactivate():
    username = session.get('username')

    result = reactivate_user(username)
    return jsonify(result)

@app.route('/api/sendMessage', methods=["POST"])
def send_message_route():
    sender_id = request.json.get('sender_id')
    recipient_id = request.json.get('recipient_id')
    content = request.json.get('content')

    result = send_message(sender_id, recipient_id, content)
    return jsonify(result)


@app.route('/api/messages', methods=['GET'])
def get_messages_route():
    username = session.get('username')
    messages = get_messages(username)
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
