import psycopg2
import os

def deactivate_user(username):
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])

    cursor = connect.cursor()
    cursor.execute("UPDATE users SET active = false WHERE username = %s", (username,))
    connect.commit()
    cursor.close()
    connect.close()

    return {"message": "User deactivated"}


def reactivate_user(username):
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])

    cursor = connect.cursor()
    cursor.execute("UPDATE users SET active = true WHERE username = %s", (username,))
    connect.commit()
    cursor.close()
    connect.close()

    return {"message": "User reactivated"}
