from bottle import route, run


@route('/')
def index():
    return """
    <title>Python Class App</title>
    Here's some info about members of the class
    """


run(reloader=True)
