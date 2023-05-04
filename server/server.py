from flask import Flask, render_template, redirect, session, request
import psycopg2

app = Flask(__name__)

app.config["SECRET_KEY"] = 'my_secret_key'


@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        identifier = request.form.get('identifier')
        password = request.form["password"]

        connect = psycopg2.connect("dbname=lovefinderrrz")
        cursor = connect.cursor()
        cursor.execute(
            "SELECT Email, UserName, Password, Admin FROM users WHERE (Email=%s OR UserName=%s) AND Password=%s",
            (identifier, identifier, password))
        user = cursor.fetchone()
        connect.close()
        if user is not None:
            session['user'] = user
            if user[3]:
                return redirect(f"/admin/{user[1]}")
            else:
                return redirect(f"/profile/{user[1]}")
        else:
            error = "Invalid username or password"
            return render_template("Login.html", error=error)
    else:
        return render_template("Login.html")


@app.route('/profile/<username>')
def profile(username):
    if 'user' in session:
        return render_template("Home.html", username=username)
    else:
        return redirect("/")


@app.route("/admin/<username>")
def admin(username):
    if "user" in session:
        return render_template("./Admin/Admin.html", username=username)
    else:
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
