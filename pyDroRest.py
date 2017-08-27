from os import getcwd
from base64 import b64decode
from bottle import Bottle, route, run, static_file, error, auth_basic


app = Bottle('pyDroRest')


def check(user, pw):
    if user == b64decode('ZWVs'):
        if pw == b64decode('aVBob25lMzgyNT8='):
            return True
    return False


@error(404)
def error404(error):
    return '404 Nothing here, sorry'


@app.route('/droPyRest', methods=['GET'])
@auth_basic(check)
def home():
    return static_file('index.html', getcwd()+'/html')


@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, getcwd())


@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, getcwd())



@app.route('/droPyRest/v0.1/front', methods=['GET'])
@auth_basic(check)
def front():
    return 'front'


@app.route('/droPyRest/v0.1/back', methods=['GET'])
@auth_basic(check)
def back():
    return 'back'


@app.route('/droPyRest/v0.1/right', methods=['GET'])
@auth_basic(check)
def right():
    return 'right'


@app.route('/droPyRest/v0.1/left', methods=['GET'])
@auth_basic(check)
def left():
    return 'left'


@app.route('/droPyRest/v0.1/frontRight', methods=['GET'])
@auth_basic(check)
def front_right():
    return 'frontRight'


@app.route('/droPyRest/v0.1/frontLeft', methods=['GET'])
@auth_basic(check)
def front_left():
    return 'frontLeft'


@app.route('/droPyRest/v0.1/backRight', methods=['GET'])
@auth_basic(check)
def back_right():
    return 'backRight'


@app.route('/droPyRest/v0.1/backLeft', methods=['GET'])
@auth_basic(check)
def back_left():
    return 'backLeft'


@app.route('/droPyRest/v0.1/up', methods=['GET'])
@auth_basic(check)
def up():
    return 'up'


@app.route('/droPyRest/v0.1/down', methods=['GET'])
@auth_basic(check)
def down():
    return 'down'


@app.route('/droPyRest/v0.1/land', methods=['GET'])
@auth_basic(check)
def land():
    return 'land'


@app.route('/droPyRest/v0.1/lift/<height:int>', methods=['GET'])
@auth_basic(check)
def lift(height):
    return 'lift ' + str(height)


run(app, host='localhost', port=1125)
