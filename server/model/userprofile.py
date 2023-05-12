import psycopg2
from psycopg2.extras import RealDictCursor
import os
import base64

def get_admin(username):
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

    cursor.close()
    connect.close()

    return admin


def search_users(search_email, search_username, search_firstname, search_lastname, search_gender, search_mobile, search_dateofbirth):
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

    cursor.close()
    connect.close()

    return results


def get_user(username):
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


