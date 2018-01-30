import sqlite3
import cgi

from bottle import route, run


def format_user(user):
    return '<div style="color: {color}">{username}</div>'.format(
        color=cgi.escape(user[2]),  # cgi.escape prevents html injection
        username=cgi.escape(user[1])
    )


@route('/')
def index():
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()

        select_statement = "SELECT * FROM users"

        c.execute(select_statement)

        users = ''.join([
            format_user(r) for r in c
        ])

    return """
    <title>Python Class App</title>
    Here's some info about members of the class
    {}
    """.format(users)


run(reloader=True)
