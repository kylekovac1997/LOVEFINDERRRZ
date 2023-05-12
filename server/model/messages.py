import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_messages(username):
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = connect.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT messenger.content, messenger.sender_id, messenger.recipient_id,
               sender.username AS sender_username, recipient.username AS recipient_username
        FROM messages AS messenger
        JOIN users AS sender ON messenger.sender_id = sender.userid
        JOIN users AS recipient ON messenger.recipient_id = recipient.userid
        WHERE messenger.sender_id = (
            SELECT userid FROM users WHERE username = %s
        ) OR messenger.recipient_id = (
            SELECT userid FROM users WHERE username = %s
        )
        ORDER BY messenger.sent_date DESC
    """, (username, username))
    messages = cursor.fetchall()
    cursor.close()
    return messages


def send_message(sender_id, recipient_id, content):
    os.environ["DATABASE_URL"] = "postgres://lovefinderrrz_bymf_user:HzaOneZ3gNyLsV7n7PF878JRi2gxibYC@dpg-chavl567avjcvo2u2sog-a.oregon-postgres.render.com/lovefinderrrz_bymf"
    connect = psycopg2.connect(os.environ["DATABASE_URL"])

    cursor = connect.cursor()
    cursor.execute("INSERT INTO messages (sender_id, recipient_id, content) VALUES (%s, %s, %s)",
                   (sender_id, recipient_id, content))
    connect.commit()
    cursor.close()

    return {"message": "Message sent successfully"}